from django.shortcuts import get_object_or_404, render,redirect

from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm

def registrar_categoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json')
    else:
        form = categoriaForm()
    return render(request,'registar.html',{'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    data =[
        {
            'id': c.id,
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data,safe=False)

def ver_categorias(request):
    return render(request,'json.html')

#Obtener uno solo de categoria 
def obtener_categoria(request,id_categoria):
    if request.method == 'GET':
        categoria= get_object_or_404(Categoria,id=id_categoria)
        data={
            'id':categoria.id,
            'nombre': categoria.nombre,
            'imagen':categoria.imagen
        }
        return JsonResponse(data,status=200)
    return JsonResponse({'Error', 'El método no es GET'},status=405)
#borrar categorias

def borrar_categoria(request,id_categoria):
    if request.method == 'DELETE':
        categoria= get_object_or_404(Categoria,id= id_categoria)
        categoria.delete()
        return JsonResponse({'mensaje': 'Categoria Eliminada Correctamente'},status=200)
    return JsonResponse({'Error','El método no es DELETE'},status=405)

import json 
def agregar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #Parametro es un texto que deberia de ser en json
            categoria =Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )# create mete directamente el objeto en la bd
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id':categoria.id
                },status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {
                    'error':str(e)
                }, status=400
            )
    # si no es Post el request
    return JsonResponse(
        {'error': 'El método no esta soportado'}, status =405
    )


#actualizar 
def actualizar_categoria(request,id_categoria):
    if request.method == 'PUT':
        categoria= get_object_or_404(Categoria,id = id_categoria)
        try:
            #La informacion de la modificacion del producto viene del body de  request
            data = json.loads(request.body)
            categoria.nombre = data.get('nombre',categoria.nombre)
            categoria.imagen = data.get('imagen', categoria.imagen)
            categoria.save()
            return JsonResponse({'mensaje': 'Categoria actualizada correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error':'Metodo no es PUT'}, status=405)
#Funciones para el método DELETE
def borrar_categoria(request, id_categoria):
    if request.method =='DELETE':
        categoria = get_object_or_404(Categoria,id=id_categoria)
        categoria.delete() # borra fisiscamente el registro de la base de datos
        return JsonResponse({'mensaje':'Categoria eleiminado correctamente'},status=200)
    return JsonResponse({'Error':'El metodo no es DELETE'}, status= 405)
#Funcion adicional para el GET