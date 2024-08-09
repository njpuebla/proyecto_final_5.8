from django.urls import path
from app import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('electricas/', views.electricas, name='Electricas'),
    path('acusticas/', views.acusticas, name='Acusticas'),
    path('amplificadores/', views.amplificadores, name='Amplificadores'),
    path('efectos/', views.efectos, name='Efectos'),
    path('buscar-electricas/', views.buscar_electricas, name="Buscar_Electricas"),
    path('buscar-acusticas/', views.buscar_acusticas, name="Buscar_Acusticas"),
    path('buscar-amplificadores/', views.buscar_amplificadores, name="Buscar_Amplificadores"),
    path('buscar-efectos/', views.buscar_efectos, name="Buscar_Efectos"),
    path('about/', views.about, name="About"),
]