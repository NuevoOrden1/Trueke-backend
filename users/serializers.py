from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'celular', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            celular=validated_data['celular'],
        )
        user.set_password(validated_data['password'])
        user.codigo_verificacion = '123456'  # Simula código
        user.save()
        # Aquí imprimirás el código en consola para simular el correo:
        print(f"Código de verificación para {user.email}: {user.codigo_verificacion}")
        return user
