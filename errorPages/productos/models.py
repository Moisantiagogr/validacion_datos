from django.db import models

# Clase de producto 
class Producto(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen= models.URLField()

    def __str__(self):
        return self.nombre
    
    #Necesito una funcion que devuelva el objeto en forma de de diccionario Dict
    def to_dict(self):
        return {
            #'claveValor': 'valor'
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
