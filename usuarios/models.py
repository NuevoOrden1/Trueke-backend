from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=128)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    calificacion_promedio = models.FloatField(default=0)
    cant_intercambios = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
