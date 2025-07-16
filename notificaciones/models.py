from django.db import models
from usuarios.models import Usuario

class TipoNotificacion(models.TextChoices):
    SOLICITUD_RECIBIDA = 'SolicitudRecibida', 'SolicitudRecibida'
    SOLICITUD_ACEPTADA = 'SolicitudAceptada', 'SolicitudAceptada'
    SOLICITUD_RECHAZADA = 'SolicitudRechazada', 'SolicitudRechazada'
    CALIFICACION_PENDIENTE = 'CalificacionPendiente', 'CalificacionPendiente'

class Notificacion(models.Model):
    usuarioDestino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.TextField()
    tipo = models.CharField(max_length=30, choices=TipoNotificacion.choices)
    leida = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def marcarComoLeida(self):
        self.leida = True
        self.save()

    def __str__(self):
        return f"{self.tipo} para {self.usuarioDestino.correo}"
