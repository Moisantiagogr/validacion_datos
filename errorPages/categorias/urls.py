from django.urls import path
from .views import *

urlpatterns =[
    path('api/get/',lista_categorias, name='lista'),
    path('json/',ver_categorias, name='json'),
    path('registrar/',registrar_categoria, name='registrar'),
    path('api/post/',agregar_categoria,name='post'),
    path('api/put/<str:id_categoria>/',actualizar_categoria, name='put'),
    path('api/delete/<str:id_categoria>/', borrar_categoria,name='delete'),
    path('api/get/<str:id_categoria>/', obtener_categoria, name='get')
]

