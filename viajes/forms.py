# viajes/forms.py

from django import forms

class BuscarViajeForm(forms.Form):
    TIPO_CHOICES = [
        ('conductor', 'Soy conductor'),
        ('pasajero', 'Necesito transporte')
    ]
    
    tipo_usuario = forms.ChoiceField(choices=TIPO_CHOICES, widget=forms.RadioSelect, label="¿Eres conductor o necesitas transporte?")
    
    destino = forms.CharField(max_length=100, required=False, label="¿Hacia dónde vas?")
    hora_salida = forms.TimeField(required=False, label="¿A qué hora necesitas el transporte?", widget=forms.TimeInput(format='%H:%M'))
    
    # Campos ocultos para latitud y longitud
    latitud = forms.DecimalField(max_digits=9, decimal_places=6, required=False)
    longitud = forms.DecimalField(max_digits=9, decimal_places=6, required=False)
