from rest_framework import serializers
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    contraseña = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'nombre', 'apellido', 'correo', 'celular',
            'contraseña', 'fotoPerfil'
        ]
        extra_kwargs = {
            'fotoPerfil': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        return Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            correo=validated_data['correo'],
            celular=validated_data['celular'],
            password=validated_data['contraseña'],  # se usa como 'contraseña' pero se pasa a .set_password()
            fotoPerfil=validated_data.get('fotoPerfil')
        )

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'nombre', 'apellido', 'correo', 'celular',
            'fotoPerfil', 'calificacionPromedio', 'cantIntercambios'
        ]
