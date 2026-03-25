from rest_framework import viewsets
from .models import CBA_Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = CBA_Cliente.objects.all()
    serializer_class = ClienteSerializer
