from rest_framework import serializers
from .models import CBA_Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBA_Cliente
        fields = '__all__'