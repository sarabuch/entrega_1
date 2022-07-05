from django.urls import path
from users.views import editarPerfil

urlpatterns =[
    path('editarPerfil/', editarPerfil, name = 'EditarPerfil'),
    ]

