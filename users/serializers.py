from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
            username=validated_data['email'],  # necesario para autenticación interna de Django
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            celular=validated_data['celular'],
        )
        user.set_password(validated_data['password'])
        user.codigo_verificacion = '123456'  # Simula código
        user.save()
        print(f"Código de verificación para {user.email}: {user.codigo_verificacion}")
        return user


#  Añade este serializador para login con email
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Esto te permitirá iniciar sesión usando el email
        request_data = self.context['request'].data
        email = request_data.get("email")
        password = request_data.get("password")

        from .models import CustomUser
        from django.contrib.auth import authenticate

        try:
            user = CustomUser.objects.get(email=email)
            attrs["username"] = user.username  # Necesario para validar con JWT
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado con ese email")

        return super().validate(attrs)

