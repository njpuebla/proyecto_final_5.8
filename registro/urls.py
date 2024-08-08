from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    
    path("registrar_usuario/", views.registro , name="Registro")

]
