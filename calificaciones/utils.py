from django.db.models import Avg
from users.models import CustomUser
from .models import Calificacion

def actualizar_promedio(usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    calificaciones = Calificacion.objects.filter(usuarioPuntuado=usuario)
    promedio = calificaciones.aggregate(prom=Avg('valor'))['prom'] or 0
    cantidad = calificaciones.count()

    usuario.calificacionPromedio = round(promedio, 2)
    usuario.cantIntercambios = cantidad
    usuario.save()