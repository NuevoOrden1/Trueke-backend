from django.contrib import admin
from .models import Objeto

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fechaPublicacion', 'usuario')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria', 'estado')