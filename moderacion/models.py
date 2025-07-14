from django.db import models
from productos.models import Objeto

class Moderador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)  # Igual que el campo password

    def __str__(self):
        return self.nombre


class RechazoModeracion(models.Model):
    objeto = models.OneToOneField(Objeto, on_delete=models.CASCADE, related_name='rechazo')
    motivo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rechazo de objeto: {self.objeto.nombre}"
