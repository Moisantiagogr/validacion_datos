import re
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

#primer formulario
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!%&$?]).{8,}$',
                'placeholder': 'Ingrese su contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'requiered': 'true'
            }
        )
    )
    password2 = forms.CharField(
        label='Repite tu Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!%&$?]).{8,}$',
                'placeholder': 'Repite tu contraseña',
                'title': 'Necesitas definir una contraseña segura',
                'requiered': 'true'
            }
        )
    )
   


    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']
        
        #Si quiero editar la forma de los inputs se necesitan los widgets
        widgets ={
            #Cada uno de los widgets del  **MODEo**
            'email': forms.EmailInput(
                #carateristicas del elemento visual
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes de ingeresar un correo valido de la UTEZ'
                }
            ), 
            'name': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'title': 'Debes de ingresar solo letras',
                    'mixlength': '3',
                    'maxlength': '50'
                }
            ),
            'surname': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'title': 'Debes de ingresar solo letras',
                    'mixlength': '3',
                    'maxlength': '50'
                }
            ),
            'control_number': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'pattern': '^[0-9]{5}[a-zA-z]{2}[0-9]{3}$',
                    'title': 'Debes de ingresar tu matricula valida de la utez',
                    'minlength': '1',
                    'maxlength':'20'
                }
            ),
            'age': forms.NumberInput(
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'title': 'Debes de ingresar solo numeros',
                    'minlength': '1',
                    'maxlength':'100'
                }
            ),
            'tel': forms.TextInput(
                attrs ={
                    'class': 'form-control',
                    'requiered': 'true',
                    'pattern': '^[0-9]{10}$',
                    'title': 'El número de télefono debe tener exactamente 10 digitos',
                    'maxlength': '10'
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', email):
            raise ValidationError("Debes de ingresar un correo válido de la UTEZ")
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if len(control_number) != 10:
            raise ValidationError("La matrícula debe tener 10 caracteres")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not re.match(r'^[0-9]{10}$', tel):
            raise ValidationError("El teléfono debe tener exactamente 10 dígitos")
        return tel

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        if not re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[!%&$?]).{8,}$', password1):
            raise ValidationError("La contraseña debe contener al menos 8 caracteres, un número, una letra mayúscula y un carácter especial")
        return password2
#Segundo formulario (inicio de sesion)        
class CustomUserLoginForm(AuthenticationForm):
   username = forms.CharField(label="Correo electrónico", max_length=150,widget=forms.EmailInput(attrs={'class': 'form-control'}))
   password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data