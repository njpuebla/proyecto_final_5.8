from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    
    path("registrar_usuario/", views.registro , name="Registro"),
    path("registro_exitoso/", views.RegisterSuccessView.as_view() , name="RegistroExitoso"),
    path('editar_usuario/', views.ModificarUsuario.as_view(), name='EditarUsuario')
    
]
