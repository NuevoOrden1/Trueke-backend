from django.urls import path
from .views import objetos_pendientes, aprobar_objeto, rechazar_objeto

urlpatterns = [
    path('pendientes/', objetos_pendientes, name='objetos_pendientes'),                   # GET /api/moderacion/pendientes
    path('aprobar/<int:id>/', aprobar_objeto, name='aprobar_objeto'),                     # PUT /api/moderacion/aprobar/:id
    path('rechazar/<int:id>/', rechazar_objeto, name='rechazar_objeto'),                  # PUT /api/moderacion/rechazar/:id
]
