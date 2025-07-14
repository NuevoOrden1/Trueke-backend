from django.urls import path
from .views import obtener_notificaciones, marcar_como_leida

urlpatterns = [
    path('<int:idUsuario>/', obtener_notificaciones, name='ver_notificaciones'),     # GET /api/notificaciones/:idUsuario
    path('<int:id>/leida/', marcar_como_leida, name='marcar_como_leida'),            # PUT /api/notificaciones/:id
]
