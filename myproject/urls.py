from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path("buscar_cfs/", views.buscar_cfs, name="buscar_cfs"),
    path("buscar_en_csv/", views.buscar_en_csv, name="bbuscar_en_csv"),
    path("buscar_vrf_rd/", views.buscar_vrf_rd, name="buscar_vrf_rd"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
