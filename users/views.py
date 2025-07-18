from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#  Vista para login con email en vez de username


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


class VerifyAccountView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        codigo = request.data.get('codigo')
        try:
            user = CustomUser.objects.get(email=email)
            if user.codigo_verificacion == codigo:
                user.verificado = True
                user.save()
                return Response({"msg": "Cuenta verificada con éxito"}, status.HTTP_200_OK)
            else:
                return Response({"error": "Código incorrecto"}, status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status.HTTP_404_NOT_FOUND)


#  Vista para login con email en vez de username
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer