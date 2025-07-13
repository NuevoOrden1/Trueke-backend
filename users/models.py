from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=20, unique=True)
    codigo_verificacion = models.CharField(max_length=6, null=True, blank=True)
    verificado = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'celular']

    def __str__(self):
        return self.email

