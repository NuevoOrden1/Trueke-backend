from django.urls import path
from .views import solicitudes_view, actualizar_estado_solicitud, intercambios_completados

urlpatterns = [
    path('', solicitudes_view, name='solicitudes'),                      # GET y POST
    path('<int:id>/', actualizar_estado_solicitud, name='actualizar_estado_solicitud'),  # PUT
    path('completados/', intercambios_completados, name='intercambios_completados'), #GET intercambios completados
]
