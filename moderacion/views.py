from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from productos.models import Objeto
from .models import RechazoModeracion
from .serializers import ObjetoPendienteSerializer, RechazoModeracionSerializer
from notificaciones.models import Notificacion
from django.shortcuts import get_object_or_404

# Ver objetos pendientes
@api_view(['GET'])
def objetos_pendientes(request):
    objetos = Objeto.objects.filter(estado='pendiente')
    serializer = ObjetoPendienteSerializer(objetos, many=True, context={'request': request})
    return Response(serializer.data)

# Aprobar objeto
@api_view(['PUT'])
def aprobar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)

    if objeto.estado != 'pendiente':
        return Response({'error': 'El objeto no está en estado pendiente'}, status=status.HTTP_400_BAD_REQUEST)

    objeto.estado = 'disponible'
    objeto.save()

    # Crear notificación de aprobación
    Notificacion.objects.create(
        usuarioDestino=objeto.usuario,
        mensaje=f"Tu objeto '{objeto.nombre}' fue aprobado y ahora está disponible.",
        tipo='aprobacion'
    )

    return Response({'mensaje': 'Objeto aprobado exitosamente'}, status=status.HTTP_200_OK)

# Rechazar objeto
@api_view(['PUT'])
def rechazar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)

    if objeto.estado != 'pendiente':
        return Response({'error': 'El objeto no está en estado pendiente'}, status=status.HTTP_400_BAD_REQUEST)

    motivo = request.data.get('motivo')
    if not motivo:
        return Response({'error': 'Debe proporcionar un motivo de rechazo'}, status=status.HTTP_400_BAD_REQUEST)

    objeto.estado = 'rechazado'
    objeto.save()

    rechazo = RechazoModeracion.objects.create(objeto=objeto, motivo=motivo)
    serializer = RechazoModeracionSerializer(rechazo)

    # Crear notificación de rechazo
    Notificacion.objects.create(
        usuarioDestino=objeto.usuario,
        mensaje=f"Tu objeto '{objeto.nombre}' fue rechazado. Motivo: {motivo}",
        tipo='rechazo'
    )

    return Response({
        'mensaje': 'Objeto rechazado',
        'rechazo': serializer.data
    }, status=status.HTTP_200_OK)
