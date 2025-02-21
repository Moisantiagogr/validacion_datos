#Gnerar todos los formularios  HTML que vamos a ocupar
from django import forms
from .models import Producto

# Crear una clase para cada fromulario que necesitemos 
class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']

    #que campos van a verse en el form


    #Personalizar mis inputs 
    widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aquí el nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen'
                }
            ),
        }

    #Etiquetas
    labels = {
        'nombre': 'Nombre del producto',
        'precio': 'Precio (MXN)',
        'imagen': 'URL de la imagen'
        }

    # Personalizar los mensajes de error 
    error_messages = {
            'precio': {
                'required': 'El precio no puede estar vacío',
                'invalid': 'Ingresa un precio válido'
            }
        }