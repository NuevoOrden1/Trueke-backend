from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Objeto
from .serializers import ObjetoSerializer

@api_view(['GET', 'POST'])
def objetos_view(request):
    if request.method == 'GET':
        objetos = Objeto.objects.all()
        serializer = ObjetoSerializer(objetos, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ObjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def obtener_objeto_por_id(request, id):
    try:
        objeto = Objeto.objects.get(pk=id)
    except Objeto.DoesNotExist:
        return Response({'error': 'Objeto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObjetoSerializer(objeto, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ObjetoSerializer(objeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'mensaje': 'Objeto eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
