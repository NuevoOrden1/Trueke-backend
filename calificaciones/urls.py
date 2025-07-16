from django.urls import path
from .views import crear_calificacion, calificaciones_usuario, editar_calificacion

urlpatterns = [
    path('', crear_calificacion, name='crear_calificacion'),
    path('<int:idUsuario>/', calificaciones_usuario, name='ver_calificaciones'),
    path('<int:id>/', editar_calificacion, name='editar_calificacion'),
]
