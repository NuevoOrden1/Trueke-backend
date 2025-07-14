from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioRegistroSerializer, UsuarioSerializer
from usuarios.models import Usuario
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def obtener_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario registrado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
