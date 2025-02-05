from django.urls import path
from .views import datos_view, buscar_cfs, buscar_en_csv, buscar_vrf_rd, pais_mercado_nodo
from myapp import views


urlpatterns = [
    path("datos/", datos_view, name="datos"),
    path("buscar_cfs/", buscar_cfs, name="buscar_cfs"),
    path("buscar_en_csv/", buscar_en_csv, name="buscar_en_csv"),
    path("buscar_vrf_rd/", buscar_vrf_rd, name="buscar_vrf_rd"),
    path("pais_mercado_nodo/", pais_mercado_nodo, name="pais_mercado_nodo"),
    path("ejecutar_ipsa/", views.ejecutar_ipsa, name="ejecutar_ipsa"),  # Nueva ruta


]
