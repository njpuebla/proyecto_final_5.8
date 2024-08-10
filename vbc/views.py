from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from app.models import Electrica

class ElectricaListView(ListView):
    model = Electrica
    context_object_name = "Electricas"
    template_name = "vbc/lista_electricas.html"
    
class ElectricaDetailView(DetailView):
    model = Electrica
    template_name = "vbc/electricas_detalle.html"
    
class ElectricaCreateView(CreateView):
    model = Electrica
    template_name = "vbc/electricas_crear.html"
    success_url = reverse_lazy("NuevaElectrica")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"]
    
class ElectricaUpdateView(UpdateView):
    model = Electrica
    template_name = "vbc/electricas_editar.html"
    success_url = reverse_lazy("EditarElectrica")
    fields = ["marca", "modelo", "serial", "anio", "precio", "descripcion"] 
    
class ElectricaDeleteView(DeleteView):
    model = Electrica
    template_name = "vbc/electricas_borrar.html"
    success_url = reverse_lazy("BorrarElectrica")