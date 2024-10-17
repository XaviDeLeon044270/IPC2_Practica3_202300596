from django.shortcuts import render
import requests
from .forms import FileForm

endpoint = 'http://localhost:5000'
# Create your views here.
def index(request):
    return render(request, 'index.html')

def cargar(request):
    return render(request, 'cargar.html')

context = {
    'contenido_archivo': None,
    'binario_xml': None,
    'mensaje_error': None,
    'mensaje_exito': None,
    'salidad_procesada': None,
}