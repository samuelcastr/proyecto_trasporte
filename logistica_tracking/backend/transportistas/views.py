from rest_framework import viewsets
from .models import CBA_Transportista
from .serializers import TransportistaSerializer

class TransportistaViewSet(viewsets.ModelViewSet):
    queryset = CBA_Transportista.objects.all()
    serializer_class = TransportistaSerializer
