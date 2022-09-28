from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.IntegerField(default=0)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombres=models.CharField(max_length=300)
    apellidos=models.CharField(max_length=300)
    dni=models.IntegerField(max_length=8)
    telefono=models.IntegerField(max_length=9)
    direccion=models.CharField(max_length=300)
    fecha_nacimiento=models.DateField('date published')
    fecha_publicacion=models.DateField('date published')

    def __str__(self):
        return self.nombres
    