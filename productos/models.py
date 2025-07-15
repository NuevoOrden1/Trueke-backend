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

    ESTADOS_MODERACION = [
    ('pendiente', 'Pendiente'),
    ('aprobado', 'Aprobado'),
    ('rechazado', 'Rechazado'),
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagenes = models.ImageField(upload_to='objetos/')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='objetos'
    )
    estadoModeracion = models.CharField(max_length=20, choices=ESTADOS_MODERACION, default='pendiente')
    motivoRechazo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre