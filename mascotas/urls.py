from django.urls import path
from mascotas.views import busqueda, Create_products
from mascotas.views import products, servicios, pacientes
from mascotas.views import Detail_product, Detail_service, Delete_product, Delete_service, Update_product, Update_service

urlpatterns =[
    path('productos/', products, name = 'products'),
    path('servicios/', servicios, name = 'servicios'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('crear-paciente/', Create_products.as_view(), name = 'crear-paciente'),
    path('busqueda/', busqueda, name = 'busqueda'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('detail-service/<int:pk>/', Detail_service.as_view(), name = 'detail_service'),
    path('delete-product/<int:pk>/', Delete_product.as_view(), name = 'delete_product'),
    path('delete-service/<int:pk>/', Delete_service.as_view(), name = 'delete_service'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
    path('update-service/<int:pk>/', Update_service.as_view(), name = 'update_service'),
    ]