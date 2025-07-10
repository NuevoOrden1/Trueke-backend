from django.contrib import admin
from .models import Objeto

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'estado', 'fecha_publicacion', 'usuario')
    search_fields = ('titulo', 'categoria')
    list_filter = ('categoria', 'estado')