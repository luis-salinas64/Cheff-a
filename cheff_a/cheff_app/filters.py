import django_filters

from cheff_app.models import *


class CtaProvFilter(django_filters.FilterSet):
    class Meta:
        
        model = CtaProv
        fields = ['id','proveedor', 'tipo_cpte']
        

class ProveedorFilter(django_filters.FilterSet):

    class Meta:
        model = Proveedor
        fields = ['nombre','codigo']
        


    