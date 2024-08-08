from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuario registrado ¡Bienvenido!')
            return redirect('Inicio')
        
        
    else:
        messages.error(request, 'El usuario no pudo ser creado por no cumplir la validación')
        form = RegistroUsuarioForm()
        
        
    return render(request, 'registro/registro.html', {'form': form })