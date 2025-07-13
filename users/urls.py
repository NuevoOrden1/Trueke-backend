from django.urls import path
from .views import UserRegistrationView, VerifyAccountView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('verify/', VerifyAccountView.as_view(), name='verify'),
]
