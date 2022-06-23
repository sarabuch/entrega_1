from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'productos', blank=True, null=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.name
    
class Servicios(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'servicios', blank=True, null=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.name
    
class Pacientes(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)
    age = models.IntegerField()
    owner = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'pacientes', blank=True, null=True)

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
    
    def __str__(self):
        return self.name