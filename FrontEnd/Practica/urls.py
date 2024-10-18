from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargar/', views.cargar, name='cargar'),
    path('cargarXML/', views.cargarXML, name='cargarXML'),
    path('cerrarAlertsCarga/', views.cerrarAlertsCarga, name='cerrarAlertsCarga'),
    path('datos/', views.datos, name='datos'),
]