from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SolicitudIntercambio
from notificaciones.models import Notificacion
from .serializers import (
    SolicitudIntercambioSerializer,
    SolicitudEnviadaSerializer,
    SolicitudRecibidaSerializer
)
from django.shortcuts import get_object_or_404


@api_view(['POST', 'GET'])
def solicitudes_view(request):
    if request.method == 'POST':
        serializer = SolicitudIntercambioSerializer(data=request.data)
        if serializer.is_valid():
            solicitud = serializer.save()
            Notificacion.objects.create(
                usuarioDestino=solicitud.receptor,
                mensaje="Has recibido una nueva solicitud de intercambio",
                tipo="solicitud"
            )
            return Response({"mensaje": "Solicitud creada correctamente", "id": serializer.instance.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        usuario_id = request.GET.get('usuarioId')
        if not usuario_id:
            return Response({"error": "Debe proporcionar usuarioId"}, status=status.HTTP_400_BAD_REQUEST)

        solicitudes_enviadas = SolicitudIntercambio.objects.filter(solicitante__id=usuario_id)
        solicitudes_recibidas = SolicitudIntercambio.objects.filter(receptor__id=usuario_id)

        data = {
            "enviadas": SolicitudEnviadaSerializer(solicitudes_enviadas, many=True, context={'request': request}).data,
            "recibidas": SolicitudRecibidaSerializer(solicitudes_recibidas, many=True, context={'request': request}).data
        }
        return Response(data)


@api_view(['PUT'])
def actualizar_estado_solicitud(request, id):
    solicitud = get_object_or_404(SolicitudIntercambio, pk=id)
    nuevo_estado = request.data.get('estado')

    if nuevo_estado not in dict(SolicitudIntercambio.ESTADOS):
        return Response({"error": "Estado inválido"}, status=status.HTTP_400_BAD_REQUEST)

    solicitud.estado = nuevo_estado
    solicitud.save()
    mensaje = f"Tu solicitud fue {nuevo_estado}"
    Notificacion.objects.create(
        usuarioDestino=solicitud.solicitante,
        mensaje=mensaje,
        tipo="estado"
    )
    return Response({"mensaje": f"Estado actualizado a {nuevo_estado}"}, status=status.HTTP_200_OK)
