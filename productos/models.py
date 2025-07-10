from django.db import models
from django.conf import settings  # referencia al modelo Usuario

class Objeto(models.Model):
    CATEGORIAS = [
        ('ropa', 'Ropa'),
        ('libros', 'Libros'),
        ('electronica', 'Electrónica'),
        ('hogar', 'Hogar'),
        ('otros', 'Otros'),
    ]

    ESTADOS = [
        ('disponible', 'Disponible'),
        ('intercambiado', 'Intercambiado'),
        ('reservado', 'Reservado'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='objetos/')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='objetos'
    )

    def __str__(self):
        return self.titulo