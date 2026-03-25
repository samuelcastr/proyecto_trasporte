from rest_framework import viewsets
from .models import CBA_Envio
from .serializers import EnvioSerializer
from tracking.models import CBA_TrackingEvento

class EnvioViewSet(viewsets.ModelViewSet):
    queryset = CBA_Envio.objects.all()
    serializer_class = EnvioSerializer
    lookup_field = 'tracking_number'

    def perform_create(self, serializer):
        instance = serializer.save()
        # Crear evento inicial de tracking
        CBA_TrackingEvento.objects.create(
            tracking_number=instance.tracking_number,
            estado=instance.estado_actual,
            ubicacion='Origen',
            descripcion=f'Envío creado con estado {instance.estado_actual}'
        )

    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_estado = old_instance.estado_actual
        instance = serializer.save()
        new_estado = instance.estado_actual
        
        # Crear evento de tracking si el estado cambió
        if old_estado != new_estado:
            CBA_TrackingEvento.objects.create(
                tracking_number=instance.tracking_number,
                estado=new_estado,
                ubicacion='Actualización manual',
                descripcion=f'Estado actualizado de {old_estado} a {new_estado}'
            )
