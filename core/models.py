from django.db import models

# Create your models here.

class Region(models.Model):
    idRegion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Ciudad(models.Model):
    idCiudad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tienda(models.Model):
    idTienda = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    nombreSucursal = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.nombre

class Lista(models.Model):
    idLista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    costoPresupuesto = models.IntegerField(default=0)
    costoReal = models.IntegerField(default=0)
    notas = models.CharField(max_length=500,default='')
    estado = models.CharField(max_length=50,default='Pendiente')
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    idLista = models.ForeignKey(Lista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
