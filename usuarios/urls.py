from django.urls import path
from .views import RegistroUsuarioView, listar_usuarios

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('listar/', listar_usuarios, name='listar_usuarios'),
]
