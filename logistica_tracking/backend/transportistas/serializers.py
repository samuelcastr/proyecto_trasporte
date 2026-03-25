from rest_framework import serializers
from .models import CBA_Transportista

class TransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBA_Transportista
        fields = '__all__'