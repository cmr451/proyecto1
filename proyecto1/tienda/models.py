from django.db import models

# Create your models here.

class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30) 
	apellidos = models.CharField(max_length = 30)
	edad = models.IntegerField()
	email = models.EmailField()

class Poducto(models.Model):
	id_producto = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	tamaño = models.CharField(max_length = 30)
	precio = models.IntegerField()
	imagen = models.ImageField(upload_to = 'photos')
	cliente = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.CASCADE)

