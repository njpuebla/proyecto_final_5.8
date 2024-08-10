from django.urls import path
from vbc import views

urlpatterns = [
    path("electricas/lista", views.ElectricaListView.as_view(), name = "ListaElectricas"),
    path("electricas/nuevo", views.ElectricaCreateView.as_view(), name = "NuevaElectrica"),
    path("electricas/<pk>", views.ElectricaDetailView.as_view(), name = "DetalleElectrica"),
    path("electricas/<pk>/editar", views.ElectricaUpdateView.as_view(), name = "EditarElectrica"),
    path("electricas/<pk>/borrar", views.ElectricaDeleteView.as_view(), name = "BorrarElectrica"),   
]