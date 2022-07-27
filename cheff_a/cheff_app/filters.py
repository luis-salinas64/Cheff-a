from turtle import textinput
import django_filters
from django.forms.widgets import TextInput

from cheff_app.models import *


class CtaProvFilter(django_filters.FilterSet):
    class Meta:
        
        model = CtaProv
        fields = ['id','proveedor', 'tipo_cpte']
        

class ProveedorFilter(django_filters.FilterSet):

    
    class Meta:
        model = Proveedor
        fields = {
            'nombre' : ['icontains'],
            'cuit': ['icontains'],
            }

class ProductoFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria']
        


    