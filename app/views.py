from django.shortcuts import render

from app.models import Electrica
from app.models import Acustica
from app.models import Amplificador
from app.models import Efecto

from app.forms import ElectricaFormulario
from app.forms import AcusticaFormulario
from app.forms import AmplificadorFormulario
from app.forms import EfectoFormulario

from app.forms import BuscaElectricaForm
from app.forms import BuscaAcusticaForm
from app.forms import BuscaAmplificadorForm
from app.forms import BuscaEfectoForm

# Create your views here.
def inicio(request):
    return render(request, "app/index.html")

def electricas(request):
    if request.method == "POST":
        el_formulario = ElectricaFormulario(request.POST)
        if el_formulario.is_valid():
            informacion = el_formulario.cleaned_data
            
            electrica = Electrica(marca=informacion["marca"], modelo=informacion["modelo"])
            electrica.save()

            return render(request, "app/index.html")
    else:
        el_formulario = ElectricaFormulario()

    return render(request, "app/electricas.html", {"el_formulario": el_formulario})

def acusticas(request):
    if request.method == "POST":
        ac_formulario = AcusticaFormulario(request.POST)
        if ac_formulario.is_valid():
            informacion = ac_formulario.cleaned_data
            
            acustica = Acustica(marca=informacion["marca"], modelo=informacion["modelo"])
            acustica.save()

            return render(request, "app/index.html")
    else:
        ac_formulario = AcusticaFormulario()

    return render(request, "app/acusticas.html", {"ac_formulario": ac_formulario})

def amplificadores(request):
    if request.method == "POST":
        am_formulario = AmplificadorFormulario(request.POST)
        if am_formulario.is_valid():
            informacion = am_formulario.cleaned_data
            
            amplificador = Amplificador(marca=informacion["marca"], modelo=informacion["modelo"])
            amplificador.save()

            return render(request, "app/index.html")
    else:
        am_formulario = AmplificadorFormulario()

    return render(request, "app/amplificadores.html", {"am_formulario": am_formulario})

def efectos(request):
    if request.method == "POST":
        ef_formulario = EfectoFormulario(request.POST)
        if ef_formulario.is_valid():
            informacion = ef_formulario.cleaned_data
            
            efecto = Efecto(marca=informacion["marca"], modelo=informacion["modelo"])
            efecto.save()

            return render(request, "app/index.html")
    else:
        ef_formulario = EfectoFormulario()

    return render(request, "app/efectos.html", {"ef_formulario": ef_formulario})

def buscar_electricas(request):
    if request.method == "POST":
        el_formulario = BuscaElectricaForm(request.POST) 

        if el_formulario.is_valid():
            informacion = el_formulario.cleaned_data
            
            electricas = Electrica.objects.filter(marca__icontains=informacion["marca"])

            return render(request, "app/mostrar_electricas.html", {"marcas": electricas})
    else:
        el_formulario = BuscaElectricaForm()

    return render(request, "app/buscar_electricas.html", {"el_formulario": el_formulario})

def buscar_acusticas(request):
    if request.method == "POST":
        ac_formulario = BuscaAcusticaForm(request.POST) 

        if ac_formulario.is_valid():
            informacion = ac_formulario.cleaned_data
            
            acusticas = Acustica.objects.filter(marca__icontains=informacion["marca"])

            return render(request, "app/mostrar_acusticas.html", {"marcas": acusticas})
    else:
        ac_formulario = BuscaAcusticaForm()

    return render(request, "app/buscar_acusticas.html", {"ac_formulario": ac_formulario})

def buscar_amplificadores(request):
    if request.method == "POST":
        am_formulario = BuscaAmplificadorForm(request.POST) 

        if am_formulario.is_valid():
            informacion = am_formulario.cleaned_data
            
            amplificadores = Amplificador.objects.filter(marca__icontains=informacion["marca"])

            return render(request, "app/mostrar_amplificadores.html", {"marcas": amplificadores})
    else:
        am_formulario = BuscaAmplificadorForm()

    return render(request, "app/buscar_amplificadores.html", {"am_formulario": am_formulario})

def buscar_efectos(request):
    if request.method == "POST":
        ef_formulario = BuscaAmplificadorForm(request.POST) 

        if ef_formulario.is_valid():
            informacion = ef_formulario.cleaned_data
            
            efectos = Efecto.objects.filter(marca__icontains=informacion["marca"])

            return render(request, "app/mostrar_efectos.html", {"marcas": efectos})
    else:
        ef_formulario = BuscaEfectoForm()

    return render(request, "app/buscar_efectos.html", {"ef_formulario": ef_formulario})