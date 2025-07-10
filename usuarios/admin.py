from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'celular', 'calificacion_promedio', 'cant_intercambios')
    search_fields = ('nombre', 'apellido', 'correo')
