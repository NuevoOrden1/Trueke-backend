from django.db import models
from productos.models import Objeto
from usuarios.models import Usuario

class SolicitudIntercambio(models.Model):
    ESTADOS = [
        ('Enviada', 'Enviada'),
        ('Propuesta', 'Propuesta'),
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
        ('Completada', 'Completada'),
    ]

    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes_enviadas')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes_recibidas')
    objetoSolicitado = models.ForeignKey(Objeto, on_delete=models.CASCADE, related_name='fue_solicitado_en')
    objetoPropuesto = models.ForeignKey(Objeto, on_delete=models.CASCADE, related_name='fue_propuesto_en')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Enviada')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.solicitante} a {self.receptor} ({self.estado})"