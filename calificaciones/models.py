from django.db import models
from users.models import CustomUser

class Calificacion(models.Model):
    VALORES = [(i, str(i)) for i in range(1, 6)]  # valores del 1 al 5

    puntuador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='calificaciones_realizadas')
    puntuado = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='calificaciones_recibidas')
    valor = models.IntegerField(choices=VALORES)
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def editar(self, nuevo_valor=None, nuevo_comentario=None):
        if nuevo_valor:
            self.valor = nuevo_valor
        if nuevo_comentario is not None:
            self.comentario = nuevo_comentario
        self.save()

    def __str__(self):
        return f"{self.puntuador} → {self.puntuado} ({self.valor})"
