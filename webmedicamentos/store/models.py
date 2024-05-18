from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    idusuario=models.IntegerField()
    nombre=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=20)
    
    
class cliente(models.Model):
    
    idcliente=models.IntegerField()
    nombre=models.CharField(max_length=40)
    telefono=models.CharField(max_length=15)
    dirección=models.CharField(max_length=30)
    idusuario=models.IntegerField()
    
    
   
class categoria(models.Model):
    idcategoria=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    
class producto(models.Model):
     idproducto=models.IntegerField()
     precio=models.floatField()
     stock=models.IntegerField()
     idcategoria=models.IntegerField()

class proveedor(models.Model):
     idproveedor=models.IntegerField()
     nombre=models.CharField(max_length=40)
     telefono=models.CharField(max_length=40)

class orden_pedido(models.Model):
    
    idproducto=models.IntegerField()
    idproveedor=models.IntegerField()
    fecha=models.DateIntegerField()
    cantidad=models.IntegerField()

class factura(models.Model):
     num_factura=models.IntegerField()
     fecha=models.DateIntegerField()
     idusuario=models.IntegerField()
     idcliente=models.IntegerField()
     iduproducto=models.IntegerField()
     cantidad=models.IntegerField()
     precio_total=models.floatField()