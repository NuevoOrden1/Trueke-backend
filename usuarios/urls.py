from django.urls import path
from .views import RegistroUsuarioView, login_view, gestionar_usuario

urlpatterns = [
    path('', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('<int:id>/', gestionar_usuario, name='gestionar_usuario'),
    path('login/', login_view, name='login_usuario'),
]
