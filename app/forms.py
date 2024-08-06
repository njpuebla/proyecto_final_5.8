from django import forms

class ElectricaFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)

class AcusticaFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)

class AmplificadorFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50) 
    
class EfectoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)   
    
class BuscaElectricaForm(forms.Form):
    marca=forms.CharField(max_length=50)
    
class BuscaAcusticaForm(forms.Form):
    marca=forms.CharField(max_length=50)    
    
class BuscaAmplificadorForm(forms.Form):
    marca=forms.CharField(max_length=50)
    
class BuscaEfectoForm(forms.Form):
    marca=forms.CharField(max_length=50)