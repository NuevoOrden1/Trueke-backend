from django.urls import path
from .views import objetos_view, objeto_detalle_view

urlpatterns = [
    path('', objetos_view, name='listar_y_crear_objetos'),            # GET y POST
    path('<int:id>/', objeto_detalle_view, name='ver_modificar_eliminar_objeto'),  # GET, PUT, DELETE
]
