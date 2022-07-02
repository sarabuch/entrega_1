from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse 

from mascotas.models import Productos, Servicios, Pacientes
from mascotas.forms import Producto_form, Servicio_form, Paciente_form
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class Create_products(LoginRequiredMixin, CreateView):
    model = Pacientes
    template_name = 'crear_paciente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('pacientes')
    

    
def busqueda(request):
    print(request.GET)
    productos = Productos.objects.filter(name__contains = request.GET['search'])
    servicios = Servicios.objects.filter(name__contains = request.GET['search'])
    pacientes = Pacientes.objects.filter(name__contains = request.GET['search'])
    context = {'productos':productos, 'servicios':servicios, 'pacientes':pacientes}
    return render(request, 'busqueda.html', context = context)  

class Detail_product(DetailView):
    model = Productos
    template_name= 'detail_product.html'

class Detail_service(DetailView):
    model = Servicios
    template_name= 'detail_service.html'

class Delete_product(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'delete_product.html'

    def get_success_url(self):
        return reverse('products.html')

class Delete_service(LoginRequiredMixin, DeleteView):
    model = Servicios
    template_name = 'delete_service.html'

    def get_success_url(self):
        return reverse('servicios.html')

class Update_product(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'update_product.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})

class Update_service(LoginRequiredMixin, UpdateView):
    model = Servicios 
    template_name = 'update_service.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_service', kwargs = {'pk':self.object.pk})

