from django import forms
from mascotas.models import Productos, Servicios, Pacientes

class Producto_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        
class Servicio_form(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'
        
class Paciente_form(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'