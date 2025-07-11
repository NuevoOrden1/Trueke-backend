from rest_framework import serializers
from .models import Objeto

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'
