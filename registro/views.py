from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserChangeForm




def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario registrado ¡Bienvenido!')
            return redirect('RegistroExitoso')
        
        
    else:
        messages.error(request, 'El usuario no pudo ser creado por no cumplir la validación')
        form = RegistroUsuarioForm()
        
        
    return render(request, 'registro/registro.html', {'form': form })


def registro_exitoso(request):

    return render(request, 'registro/pantalla_registro.html')



def edicion_exitosa(request):

    return render(request, 'registro/pantalla_edicion.html')



class RegisterSuccessView(TemplateView):
    
    template_name = 'registro/pantalla_registro.html'
    
    

class ModificarUsuario(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'registro/editar_usuario.html'
    success_url = reverse_lazy('EditarUsuario') 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El usuario ha sido modificado exitosamente.')
        return response
 
    def get_object(self, queryset=None):
        return self.request.user