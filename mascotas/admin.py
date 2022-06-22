from django.contrib import admin

from mascotas.models import Productos, Servicios, Pacientes

@admin.register(Productos)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'is_active']

@admin.register(Servicios)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'is_active']

@admin.register(Pacientes)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'age', 'owner']

#admin.site.register(Productos)
#admin.site.register(Servicios)
#admin.site.register(Pacientes)