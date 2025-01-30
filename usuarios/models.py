from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    id_epik = models.CharField(max_length=20, unique=True)  # ID de Epik para verificar estudiantes
    ubicacion = models.CharField(max_length=255)
    horario = models.CharField(max_length=255)  # Horarios habituales del usuario

    # Agregar related_name para evitar el conflicto con las relaciones inversas
    groups = models.ManyToManyField(Group, related_name="usuarios_custom", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios_permissions_custom", blank=True)

    def __str__(self):
        return self.username
