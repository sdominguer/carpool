from django.db import models
from django.contrib.auth.models import User

class Viaje(models.Model):
    conductor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viajes_conducidos')
    origen = models.CharField(max_length=255)  # Origen del viaje
    destino = models.CharField(max_length=255)  # Destino del viaje
    horario = models.DateTimeField()  # Fecha y hora del viaje
    capacidad = models.IntegerField()  # Capacidad del vehículo
    pasajeros = models.ManyToManyField(User, related_name='viajes_pasajero', blank=True)  # Pasajeros

    def __str__(self):
        return f'Viaje de {self.conductor.username} de {self.origen} a {self.destino}'
