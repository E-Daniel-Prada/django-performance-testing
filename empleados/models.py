from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    

