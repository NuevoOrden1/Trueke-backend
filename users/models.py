from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=20, unique=True)
    codigo_verificacion = models.CharField(max_length=6, null=True, blank=True)
    verificado = models.BooleanField(default=False)
    # Campos migrados de usuarios.Usuario
    fotoPerfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    calificacionPromedio = models.FloatField(default=0)
    cantIntercambios = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'celular']

    def __str__(self):
        return self.email

