from django.urls import path
from . import views

pp_name = 'pagos'  # Esto es lo que define el namespace

urlpatterns = [
    path('pago/<int:viaje_id>/', views.realizar_pago, name='realizar_pago'),
]
