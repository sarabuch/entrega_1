from django.urls import path
from mascotas.views import busqueda, crear_producto, crear_servicio, crear_paciente
from mascotas.views import products, servicios, pacientes

urlpatterns =[
    path('productos/', products, name = 'products'),
    path('servicios/', servicios, name = 'servicios'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('crear-producto/', crear_producto, name = 'crear-producto'),
    path('crear-servicio/', crear_servicio, name = 'crear-servicio'),
    path('crear-paciente/', crear_paciente, name = 'crear-paciente'),
    path('busqueda/', busqueda, name = 'busqueda'),
]