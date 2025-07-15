from django.db import models
from django.conf import settings

class Objeto(models.Model):
    CATEGORIAS = [
        ('ropa', 'Ropa'),
        ('libros', 'Libros'),
        ('electronica', 'Electrónica'),
        ('hogar', 'Hogar'),
        ('otros', 'Otros'),
    ]

    ESTADOS = [
        ('pendiente', 'Pendiente'),         # Producto recién publicado, esperando revisión
        ('disponible', 'Disponible'),       # Aprobado por el moderador
        ('rechazado', 'Rechazado'),         # Rechazado por el moderador
        ('reservado', 'Reservado'),         # Reservado por alguien
        ('intercambiado', 'Intercambiado'), # Ya intercambiado
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagenes = models.ImageField(upload_to='objetos/')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='objetos'
    )

    def __str__(self):
        return self.nombre
