from django.shortcuts import render
import requests
from .forms import FileForm

endpoint = 'http://localhost:5000'
# Create your views here.
def index(request):
    return render(request, 'index.html')

def cargar(request):
    return render(request, 'cargar.html')

def datos(request):
    return render(request, 'datos.html')

context = {
    'contenido_archivo': None,
    'binario_xml': None,
    'mensaje_error': None,
    'mensaje_exito': None,
    'salidad_procesada': None,
}

def cargarXML(request):
    try:
        if request.method == 'POST':
            # Se obtiene el archivo del formulario
            form = FileForm(request.POST, request.FILES)
            # Se valida el formulario
            if form.is_valid():
                # Se obtiene el archivo del formulario
                archivo = request.FILES['file']
                # Se lee el contenido del archivo
                contenido = archivo.read()
                # Se decodifica el archivo a utf-8
                contenido_xml = contenido.decode('utf-8')
                # Se almacena el contenido del archivo en el contexto
                context['contenido_archivo'] = contenido_xml
                context['binario_xml'] = contenido
                # Se almacenan los mensajes de éxito y error en el contexto
                context['mensaje_exito'] = 'Archivo cargado con éxito'
                context['mensaje_error'] = None
                return render(request, 'cargar.html', context)
    except:
        context['mensaje_exito'] = None
        context['mensaje_error'] = 'Error al cargar el archivo'
        return render(request, 'cargar.html', context)

def cerrarAlertsCarga(request):
    context['mensaje_exito'] = None
    context['mensaje_error'] = None
    return render(request, 'cargar.html', context)

def procesarXML(request):
    try:
        if request.method == 'POST':
            # Se obtiene el archivo del formulario
            archivo = context['binario_xml']
            # Se valida el formulario
            if archivo is None:
                context['mensaje_exito'] = None
                context['mensaje_error'] = 'Error al enviar el archivo'
                return render(request, 'cargar.html', context)
            response = requests.post(endpoint + '/procesarXML', files={'file': archivo})
    except:
        context['mensaje_exito'] = None
        context['mensaje_error'] = 'Error al procesar el archivo'
        return render(request, 'cargar.html', context)