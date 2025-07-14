from rest_framework import serializers
from .models import Notificacion

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = [
            'id',
            'usuarioDestino',
            'mensaje',
            'tipo',
            'leida',
            'fecha'
        ]
        read_only_fields = ['id', 'fecha', 'leida']
