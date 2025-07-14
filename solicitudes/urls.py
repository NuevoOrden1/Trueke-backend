from django.urls import path
from .views import solicitudes_view, actualizar_estado_solicitud

urlpatterns = [
    path('', solicitudes_view, name='solicitudes'),                      # GET y POST
    path('<int:id>/', actualizar_estado_solicitud, name='actualizar_estado_solicitud'),  # PUT
]
