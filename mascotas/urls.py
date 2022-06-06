from django.urls import path
from mascotas.views import crear_producto, crear_servicio, crear_paciente, buscar_producto
from mascotas.views import products, servicios, pacientes

urlpatterns =[
    path('productos/', products, name = 'products'),
    path('servicios/', servicios, name = 'servicios'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('crear-producto/', crear_producto, name = 'crear-producto'),
    path('crear-servicio/', crear_servicio, name = 'crear-servicio'),
    path('crear-paciente/', crear_paciente, name = 'crear-paciente'),
    path('buscar-producto/', buscar_producto, name = 'buscar-producto')
]