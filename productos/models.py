from django.db import models
from empleados.models import Empleado

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    empleados = models.ManyToManyField(Empleado)
    
    def __str__(self):
        return self.nombre
    