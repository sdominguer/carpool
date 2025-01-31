from django.shortcuts import render, redirect
from .forms import BuscarViajeForm

# viajes/views.py

from django.shortcuts import render, redirect
from .forms import BuscarViajeForm

def buscar_viajes(request):
    if request.method == 'POST':
        form = BuscarViajeForm(request.POST)
        
        if form.is_valid():
            tipo_usuario = form.cleaned_data['tipo_usuario']
            destino = form.cleaned_data['destino']
            hora_salida = form.cleaned_data['hora_salida']
            latitud = form.cleaned_data['latitud']
            longitud = form.cleaned_data['longitud']
            
            # Aquí puedes usar latitud y longitud para realizar una búsqueda de viajes cercanos, por ejemplo
            print(f'Destino: {destino}, Latitud: {latitud}, Longitud: {longitud}')
            
            return redirect('viajes:resultado_busqueda')
    else:
        form = BuscarViajeForm()

    return render(request, 'viajes/buscar.html', {'form': form})


# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')
