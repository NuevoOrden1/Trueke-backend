from rest_framework import serializers
from .models import Moderador, RechazoModeracion
from productos.models import Objeto

class ModeradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderador
        fields = ['id', 'nombre', 'correo', 'contraseña']
        extra_kwargs = {
            'contraseña': {'write_only': True}
        }

class ObjetoPendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = ['id', 'nombre', 'descripcion', 'categoria', 'imagenes', 'estado', 'fechaPublicacion', 'usuario']

class RechazoModeracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RechazoModeracion
        fields = ['id', 'objeto', 'motivo', 'fecha']