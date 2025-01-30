
from django.urls import path
from . import views

app_name = 'viajes'

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('buscar/', views.buscar_viajes, name='buscar_viajes'),  # Buscar viajes
    path('detalle/<int:viaje_id>/', views.detalle_viaje, name='detalle_viaje'),  # Ver detalles del viaje
    path('unirse/<int:viaje_id>/', views.unirse_a_viaje, name='unirse_a_viaje'),  # Unirse a un viaje
]
