from django.shortcuts import render
from django.http import HttpResponse
from .utils import google_search
#from .models import Usuarios
# Create your views here.
from django.http import JsonResponse
from .models import ErrorLog
#def index(request):#   return HttpResponse("<h1> Hola mundo !</h1>")

def index(request):
    return render(request,'index.html', status=200)

def error_404_view(request,exception):
    return render(request,'404.html',status=404)

def error_500_view(request,exception):
    return render(request,'500.html',status=500)

def generar_error(request):
    return 7/0

def onePage (request):
    return render(request,'onePage.html',status=200)

def prueba_front(request):
    texto = request.GET.get('texto','')
    #vamos a generar información en python
    objeto1={
        'id':'001',
        'titulo':texto,
        'descripcion':'text generico 1'
    }
    objecto2={
        'id':'002',
        'titulo':'primer titulo2',
        'descripcion':'text generico 2'
    }
    objecto3={
        'id':'003',
        'titulo':'primer titulo3',
        'descripcion':'text generico 3'
    }
    
    conjunto =[objeto1,objecto2,objecto3]

    # como mandar un objeto (variable)python a la vista

    #obtener los datos de la DB 
   # personas = Usuarios.objects.values('id','nombres','apellidos','edad')listaPersonas =list(personas)

    return render(
        request,
        'prueba.html',
        {'objeto':objeto1,'arreglo':conjunto},
    )

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})