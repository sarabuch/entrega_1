from django.contrib import admin

from mascotas.models import Productos, Servicios, Pacientes

# Register your models here.
admin.site.register(Productos)
admin.site.register(Servicios)
admin.site.register(Pacientes)