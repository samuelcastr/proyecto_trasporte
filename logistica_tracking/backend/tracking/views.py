from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CBA_TrackingEvento
from .serializers import TrackingEventoSerializer
from envios.models import CBA_Envio
from datetime import datetime, timedelta
import requests

class TrackingEventView(APIView):
    def post(self, request):
        serializer = TrackingEventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackingHistoryView(APIView):
    def get(self, request, tracking_number):
        eventos = CBA_TrackingEvento.objects.filter(tracking_number=tracking_number).order_by('-fecha_evento')
        serializer = TrackingEventoSerializer(eventos, many=True)
        return Response(serializer.data)

class TrackingStatusView(APIView):
    def get(self, request, tracking_number):
        try:
            envio = CBA_Envio.objects.get(tracking_number=tracking_number)
            ultimo_evento = CBA_TrackingEvento.objects.filter(tracking_number=tracking_number).order_by('-fecha_evento').first()
            if ultimo_evento:
                data = {
                    "tracking_number": tracking_number,
                    "status": ultimo_evento.estado,
                    "last_location": ultimo_evento.ubicacion,
                    "estimated_delivery": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
                }
            else:
                data = {
                    "tracking_number": tracking_number,
                    "status": envio.estado_actual,
                    "last_location": envio.origen,
                    "estimated_delivery": (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
                }
            return Response(data)
        except CBA_Envio.DoesNotExist:
            return Response({"error": "Envío no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class TrackingSyncView(APIView):
    def post(self, request, tracking_number):
        try:
            envio = CBA_Envio.objects.get(tracking_number=tracking_number)
            # Consumir API externa
            url = f"http://127.0.0.1:8000/external-api/tracking/{tracking_number}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Actualizar estado del envío
                envio.estado_actual = data['status']
                envio.save()
                # Guardar evento
                evento = CBA_TrackingEvento.objects.create(
                    tracking_number=tracking_number,
                    estado=data['status'],
                    ubicacion=data['location'],
                    descripcion=f"Sincronizado desde API externa: {data['status']}"
                )
                return Response({"message": "Sincronización exitosa", "data": data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Error en API externa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except CBA_Envio.DoesNotExist:
            return Response({"error": "Envío no encontrado"}, status=status.HTTP_404_NOT_FOUND)
