from django.urls import path
from .views import subscribe, email_temp

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('email_temp/', email_temp, name='email_temp'),
]
