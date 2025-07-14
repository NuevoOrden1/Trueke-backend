from django.urls import path
from .views import objetos_view, obtener_objeto_por_id

urlpatterns = [
    path('', objetos_view, name='listar_y_crear_objetos'),
    path('<int:id>/', obtener_objeto_por_id, name='ver_editar_eliminar_objeto'),
]
