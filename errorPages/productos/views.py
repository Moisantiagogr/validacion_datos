from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto
# Este objeto me permite eviar respuestas JSON
from django.http import JsonResponse

from .forms import productoForm
## una vista que cargue y maneje el formulario
def agregar_producto(request):
    # checar si vengo del from 
    if request.method == 'POST':
        form = productoForm(request.POST)
        #checar que sus datos esten bien 
        if form.is_valid():
            #lo guardo
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    return render(request,'agregar.html',{'form': form})
# Create your views here.
#Vista que devueleve los productos coo JSON
def lista_productos(request):
    #Obtener todos los objetos de los produtos de la bd
    productos = Producto.objects.all()

    #vamos a guardar los datos en un diccionario
    # Este diccionario fue creado al aire y no es seguro 
    data =[
        {
            'id':p.id,
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    return JsonResponse(data,safe=False)


def ver_productos(request):
    return render(request,'ver.html')

#funcion que agrega un producto con un objeto JSON
import json
def registar_producto(request):
    #Checar si la request es de tipo POST
    if request.method == 'POST':
        # quiere decir que si estoy manejando el rquest
        try:
            data = json.loads(request.body) #Parametro es un texto que deberia de ser en json
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )# create mete directamente el objeto en la bd
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoro',
                    'id':producto.id
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

#Funciones para el método PUT
def actualizar_producto(request,id_producto):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto,id = id_producto)
        try:
            #La informacion de la modificacion del producto viene del body de  request
            data = json.loads(request.body)
            producto.nombre = data.get('nombre',producto.nombre)
            producto.precio= data.get('precio',producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse({'mensaje': 'Producto actualizado correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error':'Metodo no es PUT'}, status=405)
#Funciones para el método DELETE
def borrar_producto(request, id_producto):
    if request.method =='DELETE':
        producto = get_object_or_404(Producto,id=id_producto)
        producto.delete() # borra fisiscamente el registro de la base de datos
        return JsonResponse({'mensaje':'Prodcto eleiminado correctamente'},status=200)
    return JsonResponse({'Error':'El metodo no es DELETE'}, status= 405)
#Funcion adicional para el GET
#De retornar un producto especifico 
def obtener_producto(request, id_producto):
    if  request.method =='GET':
        producto= get_object_or_404(Producto, id=id_producto)
        data ={
            'id':producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'Error':'El metodo no es Get'}, status=405)