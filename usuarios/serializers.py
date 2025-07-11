from rest_framework import serializers
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'celular', 'password', 'foto_perfil']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Usa el método create_user del modelo para manejar hashing de contraseña
        return Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            correo=validated_data['correo'],
            celular=validated_data['celular'],
            password=validated_data['password'],
            foto_perfil=validated_data.get('foto_perfil')
        )

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'celular', 'foto_perfil', 'calificacion_promedio', 'cant_intercambios']
