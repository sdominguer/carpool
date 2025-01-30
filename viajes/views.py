from django.shortcuts import render,redirect
from .models import Viaje
#from carpool.ml.matching import obtener_viajes_por_cluster  # O el algoritmo que estés utilizando
from django.shortcuts import get_object_or_404

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para la búsqueda de viajes
def buscar_viajes(request):
    # Obtener los viajes agrupados por el algoritmo de K-Means
    #viajes_por_cluster = obtener_viajes_por_cluster()
    return render(request, 'viajes/buscar.html', {'viajes_por_cluster': viajes_por_cluster})

def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)
    return render(request, 'viajes/detalle_viaje.html', {'viaje': viaje})

def unirse_a_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)
    
    if request.method == 'POST':
        if viaje.pasajeros.filter(id=request.user.id).exists():
            return redirect('viajes:detalle_viaje', viaje_id=viaje.id)
        
        viaje.pasajeros.add(request.user)
        return redirect('viajes:detalle_viaje', viaje_id=viaje.id)
    
    return render(request, 'viajes/unirse_viaje.html', {'viaje': viaje})
