from django.shortcuts import render, redirect
# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UsuarioCreationForm
from .models import Usuario

def registro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Crear el usuario
            login(request, usuario)  # Iniciar sesión automáticamente después de registrar
            return redirect('carpool:solicitar_viaje')  # Redirigir a la página de solicitar viaje
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


# usuarios/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('carpool:solicitar_viaje')  # Redirigir a la página de solicitar viaje
            else:
                # Manejar el caso de error (usuario no encontrado)
                return redirect('usuarios:login')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


# usuarios/views.py
from django.shortcuts import render

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('usuarios:login')  # Redirigir a la página de login si no está autenticado
    return render(request, 'usuarios/perfil.html')
