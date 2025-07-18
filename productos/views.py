from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Objeto
from .serializers import ObjetoSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def objetos_view(request):
    if request.method == 'GET':
        objetos = Objeto.objects.all()
        serializer = ObjetoSerializer(objetos, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':  # publicar()
        data = request.data.copy()
        data['estado'] = 'pendiente'  # forzamos estado inicial
        serializer = ObjetoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def objeto_detalle_view(request, id):
    objeto = get_object_or_404(Objeto, pk=id)

    if request.method == 'GET':
        serializer = ObjetoSerializer(objeto, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':  # modificar()
        serializer = ObjetoSerializer(objeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'mensaje': 'Objeto eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
