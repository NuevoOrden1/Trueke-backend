from rest_framework import serializers
from .models import SolicitudIntercambio


class SolicitudIntercambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudIntercambio
        fields = '__all__'


class SolicitudEnviadaSerializer(serializers.ModelSerializer):
    objetoSolicitado_nombre = serializers.CharField(source='objetoSolicitado.titulo', read_only=True)
    objetoSolicitado_imagen = serializers.ImageField(source='objetoSolicitado.imagen', read_only=True)
    objetoPropuesto_nombre = serializers.CharField(source='objetoPropuesto.titulo', read_only=True)
    objetoPropuesto_imagen = serializers.ImageField(source='objetoPropuesto.imagen', read_only=True)

    class Meta:
        model = SolicitudIntercambio
        fields = [
            'id',
            'estado',
            'objetoSolicitado_nombre',
            'objetoSolicitado_imagen',
            'objetoPropuesto_nombre',
            'objetoPropuesto_imagen'
        ]


class SolicitudRecibidaSerializer(serializers.ModelSerializer):
    objetoSolicitado_nombre = serializers.CharField(source='objetoSolicitado.titulo', read_only=True)
    objetoSolicitado_imagen = serializers.ImageField(source='objetoSolicitado.imagen', read_only=True)
    objetoPropuesto_nombre = serializers.CharField(source='objetoPropuesto.titulo', read_only=True)
    objetoPropuesto_imagen = serializers.ImageField(source='objetoPropuesto.imagen', read_only=True)
    solicitante_nombre = serializers.CharField(source='solicitante.nombre', read_only=True)
    solicitante_apellido = serializers.CharField(source='solicitante.apellido', read_only=True)

    class Meta:
        model = SolicitudIntercambio
        fields = [
            'id',
            'estado',
            'objetoSolicitado_nombre',
            'objetoSolicitado_imagen',
            'objetoPropuesto_nombre',
            'objetoPropuesto_imagen',
            'solicitante_nombre',
            'solicitante_apellido'
        ]

class IntercambioCompletadoSerializer(serializers.ModelSerializer):
    objetoSolicitado_nombre = serializers.CharField(source='objetoSolicitado.nombre', read_only=True)
    objetoPropuesto_nombre = serializers.CharField(source='objetoPropuesto.nombre', read_only=True)
    objetoSolicitado_imagen = serializers.ImageField(source='objetoSolicitado.imagenes', read_only=True)
    objetoPropuesto_imagen = serializers.ImageField(source='objetoPropuesto.imagenes', read_only=True)
    solicitante_nombre = serializers.CharField(source='solicitante.nombre', read_only=True)
    receptor_nombre = serializers.CharField(source='receptor.nombre', read_only=True)

    class Meta:
        model = SolicitudIntercambio
        fields = [
            'id', 'estado', 'objetoSolicitado_nombre', 'objetoSolicitado_imagen',
            'objetoPropuesto_nombre', 'objetoPropuesto_imagen',
            'solicitante_nombre', 'receptor_nombre', 'fecha'
        ]