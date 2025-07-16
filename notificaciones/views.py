from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notificacion
from .serializers import NotificacionSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def obtener_notificaciones(request, idUsuario):
    notificaciones = Notificacion.objects.filter(usuarioDestino=idUsuario).order_by('-fecha')
    serializer = NotificacionSerializer(notificaciones, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def marcar_como_leida(request, id):
    notificacion = get_object_or_404(Notificacion, pk=id)
    if not notificacion.leida:
        notificacion.leida = True
        notificacion.save()
        return Response({"mensaje": "Notificación marcada como leída"}, status=status.HTTP_200_OK)
    else:
        return Response({"mensaje": "La notificación ya estaba marcada como leída"}, status=status.HTTP_200_OK)
