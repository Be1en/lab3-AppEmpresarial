from django.db import models

class Proveedor(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    direccion_calle = models.CharField(max_length=100)
    direccion_numero = models.CharField(max_length=10)
    direccion_comuna = models.CharField(max_length=50)
    direccion_ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()

class Cliente(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    direccion_calle = models.CharField(max_length=100)
    direccion_numero = models.CharField(max_length=10)
    direccion_comuna = models.CharField(max_length=50)
    direccion_ciudad = models.CharField(max_length=50)

class TelefonoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Venta(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

class ProductoVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_vendida = models.PositiveIntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

