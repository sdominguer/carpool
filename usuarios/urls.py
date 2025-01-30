
# usuarios/urls.py
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]
