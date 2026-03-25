from rest_framework import serializers
from .models import CBA_TrackingEvento

class TrackingEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBA_TrackingEvento
        fields = '__all__'