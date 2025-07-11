from django.urls import path
from .views import crear_objeto, listar_objetos

urlpatterns = [
    path('crear/', crear_objeto, name='crear_objeto'),
    path('listar/', listar_objetos, name='listar_objetos'),
]
