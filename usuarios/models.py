from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, celular, password=None, **extra_fields):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        correo = self.normalize_email(correo)
        user = self.model(
            correo=correo,
            nombre=nombre,
            apellido=apellido,
            celular=celular,
            **extra_fields
        )
        user.set_password(password)  # Importante: convierte la contraseña en hash
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, apellido, celular, password):
        user = self.create_user(correo, nombre, apellido, celular, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    fotoPerfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)  # nombre del diagrama
    calificacionPromedio = models.FloatField(default=0)  # nombre del diagrama
    cantIntercambios = models.IntegerField(default=0)    # nombre del diagrama

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'celular']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
