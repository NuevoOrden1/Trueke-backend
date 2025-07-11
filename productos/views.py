from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Objeto
from .serializers import ObjetoSerializer

@api_view(['POST'])
def crear_objeto(request):
    serializer = ObjetoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_objetos(request):
    objetos = Objeto.objects.all()
    serializer = ObjetoSerializer(objetos, many=True, context={'request': request})
    return Response(serializer.data)