from rest_framework import serializers
from .models import CBA_Envio

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBA_Envio
        fields = '__all__'