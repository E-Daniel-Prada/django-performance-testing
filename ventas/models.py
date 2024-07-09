from django.db import models
from clientes.models import Cliente
from productos.models import Producto

# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    producto = models.ManyToManyField(Producto)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField()

