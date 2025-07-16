from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioRegistroSerializer, UsuarioSerializer
from usuarios.models import Usuario
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

@api_view(['GET', 'PUT', 'DELETE'])
def gestionar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioRegistroSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario actualizado correctamente"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response({"mensaje": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario registrado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    correo = request.data.get('correo')
    contraseña = request.data.get('contraseña')

    if not correo or not contraseña:
        return Response({'error': 'Correo y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = authenticate(request, username=correo, password=contraseña)

    if usuario is not None:
        serializer = UsuarioSerializer(usuario)
        return Response({
            'mensaje': 'Inicio de sesión exitoso',
            'usuario': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
