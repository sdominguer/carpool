from django.shortcuts import render, get_object_or_404
from .models import Pago
from viajes.models import Viaje

def realizar_pago(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)
    
    if request.method == 'POST':
        monto = viaje.capacidad * 0.1  # Ejemplo de cálculo de costo
        pago = Pago.objects.create(pasajero=request.user, viaje=viaje, monto=monto)
        return render(request, 'pagos/pago_exitoso.html', {'pago': pago})
    
    return render(request, 'pagos/realizar_pago.html', {'viaje': viaje})
