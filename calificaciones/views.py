from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Calificacion
from .serializers import CalificacionSerializer
from django.shortcuts import get_object_or_404
from .utils import actualizar_promedio

# Crear una calificación
@api_view(['POST'])
def crear_calificacion(request):
    serializer = CalificacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        actualizar_promedio(serializer.instance.usuarioPuntuado.id)
        return Response({"mensaje": "Calificación creada correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Ver calificaciones recibidas por un usuario
@api_view(['GET'])
def calificaciones_usuario(request, idUsuario):
    calificaciones = Calificacion.objects.filter(puntuado__id=idUsuario)
    serializer = CalificacionSerializer(calificaciones, many=True)
    return Response(serializer.data)

# Editar una calificación existente (solo comentario o valor)
@api_view(['PUT'])
def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, pk=id)
    serializer = CalificacionSerializer(calificacion, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        actualizar_promedio(serializer.instance.usuarioPuntuado.id)
        return Response({"mensaje": "Calificación actualizada correctamente"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
