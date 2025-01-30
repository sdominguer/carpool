from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('viajes/', include('viajes.urls')),  # Cambiado de 'carpool' a 'viajes'
    path('pagos/', include('pagos.urls')),

    # Ruta vacía para la página de inicio
    path('', include('viajes.urls')),  # Redirigir al home desde viajes
]
