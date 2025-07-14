from django.urls import path
from .views import RegistroUsuarioView, obtener_usuario_por_id

urlpatterns = [
    path('', RegistroUsuarioView.as_view(), name='registro_usuario'),                  # POST /api/usuarios
    path('<int:id>/', obtener_usuario_por_id, name='obtener_usuario_por_id'),          # GET /api/usuarios/1
]