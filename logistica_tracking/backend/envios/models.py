from django.db import models
from clientes.models import CBA_Cliente
from transportistas.models import CBA_Transportista

class CBA_Envio(models.Model):
    ESTADOS = [
        ('registrado', 'Registrado'),
        ('en_transito', 'En Tránsito'),
        ('centro_distribucion', 'Centro de Distribución'),
        ('en_reparto', 'En Reparto'),
        ('entregado', 'Entregado'),
        ('incidente', 'Incidente'),
    ]

    tracking_number = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(CBA_Cliente, on_delete=models.CASCADE)
    transportista = models.ForeignKey(CBA_Transportista, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado_actual = models.CharField(max_length=20, choices=ESTADOS, default='registrado')

    def __str__(self):
        return self.tracking_number
