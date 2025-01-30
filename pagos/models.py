from django.db import models
from django.contrib.auth.models import User
from viajes.models import Viaje

class Pago(models.Model):
    pasajero = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos')
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Permitir valores nulos
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago de {self.pasajero.username} por el viaje de {self.viaje.conductor.username}'
