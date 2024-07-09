from empleados.models import Empleado
from clientes.models import Cliente
from productos.models import Producto
from ventas.models import Venta


def test_len():
    # No aplicar
    print(len(Venta.objects.all()))
    # aplicar
    print(Venta.objects.count())