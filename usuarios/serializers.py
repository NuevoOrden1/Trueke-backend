from rest_framework import serializers
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo', 'celular', 'password', 'foto_perfil']
        extra_kwargs = {
            'password': {'write_only': True},
            'foto_perfil': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        return Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            correo=validated_data['correo'],
            celular=validated_data['celular'],
            password=validated_data['password'],
            foto_perfil=validated_data.get('foto_perfil', None)
        )

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'nombre', 'apellido', 'correo', 'celular',
            'foto_perfil', 'calificacion_promedio', 'cant_intercambios'
        ]
