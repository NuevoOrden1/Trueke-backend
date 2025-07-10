from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'celular', 'contrasena', 'foto_perfil']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }

    def create(self, validated_data):
        # Encripta la contraseña antes de guardar
        validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super().create(validated_data)
