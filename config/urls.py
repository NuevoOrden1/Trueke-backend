"""
URL configuration for the Trueke project backend..

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # add por Ods
from django.conf.urls.static import static # add por Ods

urlpatterns = [
    path('admin/', admin.site.urls),
    # Endpoints para usuarios
    path('api/users/', include('users.urls')),
    # Endpoints para objetos/productos
    path('api/objetos/', include('productos.urls')),
    # Endpoints para solicitudes de intercambio
    path('api/solicitudes/', include('solicitudes.urls')),
    # Endpoints para notificaciones
    path('api/notificaciones/', include('notificaciones.urls')),
    # Endpoints para moderador
    path('api/moderacion/', include('moderacion.urls')),
    # Endpoints para calificaciones
    path('api/calificaciones/', include('calificaciones.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


