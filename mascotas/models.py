from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    
    
class Servicios(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    
    
class Pacientes(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)
    age = models.IntegerField()
    owner = models.CharField(max_length=40)