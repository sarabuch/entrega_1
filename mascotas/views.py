from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from mascotas.models import Productos, Servicios, Pacientes
from mascotas.forms import Producto_form, Servicio_form, Paciente_form


# Create your views here.
def products(request):
    print(request.method)
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)

def servicios(request):
    print(request.method)
    servicios = Servicios.objects.all()
    context = {'servicios':servicios}
    return render(request, 'servicios.html', context=context)

def pacientes(request):
    print(request.method)
    pacientes = Pacientes.objects.all()
    context = {'pacientes':pacientes}
    return render(request, 'pacientes.html', context=context)

def crear_producto(request):
    if request.method == 'GET':
        form = Producto_form()
        context = {'form':form}
        return render(request, 'crear_producto.html', context=context)
    else:
        form = Producto_form(request.POST)
        if form.is_valid():
            new_product = Productos.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
            )
            context ={'new_product':new_product}
        return render(request, 'crear_producto.html', context=context)
    
def crear_servicio(request):
    if request.method == 'GET':
        form = Servicio_form()
        context = {'form':form}
        return render(request, 'crear_servicio.html', context=context)
    else:
        form = Servicio_form(request.POST)
        if form.is_valid():
            new_service = Servicios.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
            )
            context ={'new_service':new_service}
        return render(request, 'crear_servicio.html', context=context)
    
def crear_paciente(request):
    if request.method == 'GET':
        form = Paciente_form()
        context = {'form':form}
        return render(request, 'crear_paciente.html', context=context)
    else:
        form = Paciente_form(request.POST)
        if form.is_valid():
            new_patient = Pacientes.objects.create(
                name = form.cleaned_data['name'],
                species = form.cleaned_data['species'],
                age = form.cleaned_data['age'],
                owner = form.cleaned_data['owner'],
            )
            context ={'new_patient':new_patient}
        return render(request, 'crear_paciente.html', context=context)
    
def busqueda(request):
    print(request.GET)
    productos = Productos.objects.filter(name__contains = request.GET['search'])
    servicios = Servicios.objects.filter(name__contains = request.GET['search'])
    pacientes = Pacientes.objects.filter(name__contains = request.GET['search'])
    context = {'productos':productos, 'servicios':servicios, 'pacientes':pacientes}
    return render(request, 'busqueda.html', context = context)  

