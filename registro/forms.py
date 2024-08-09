from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
   
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    username = forms.CharField(label='Usuario', required=True)
    email = forms.EmailField(required=True)
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    

    class Meta:
        
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class CustomUserChangeForm(UserChangeForm):
    
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    username = forms.CharField(label='Usuario', required=True)
    email = forms.EmailField(required=True)
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        