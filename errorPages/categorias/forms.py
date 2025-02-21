from django import forms
from .models import Categoria

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','imagen']


        widgets ={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese aquí el nombre de la categoria'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen'
                }
            )
        }

        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre no puede estar vacío',
                'invalid': 'Ingresa un nombre válido'
            }
        }
