from rest_framework import serializers
from .models import Objeto

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'categoria',
            'imagenes',
            'estado',
            'fechaPublicacion',
            'usuario'
        ]
        read_only_fields = ['id', 'fechaPublicacion']
