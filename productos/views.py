from rest_framework.decorators import api_view
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
        serializer = ObjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
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
