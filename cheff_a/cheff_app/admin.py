from django.contrib import admin
from cheff_app.models import *

@admin.register(Comprobante)
class Comprobante(admin.ModelAdmin):
    search_fields = ['tipo']
    ordering = ['tipo']
    list_display = ('id','tipo')


@admin.register(Proveedor)
class Proveedor(admin.ModelAdmin):

    search_fields = ['nombre']
    ordering = ['nombre']
    list_display = ('id','nombre','cuit','telefono')

    
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','codigo','nombre')


@admin.register(UnMedida)
class UnMedida(admin.ModelAdmin):
    search_fields = ['un_medida']
    list_display = ('id','un_medida')


@admin.register(Producto)
class Producto(admin.ModelAdmin):
    
    list_display = ('id','codigo','nombre')

     # NOTE: Filtro lateral de elementos:
    list_filter= ('nombre','categoria')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['nombre']
    

@admin.register(Mesa)
class Mesa(admin.ModelAdmin):
    list_display = ('id','numero','capacidad','descripcion')

@admin.register(Moza_o)
class Moza_o(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','legajo','nombre','fecha_ingreso')

@admin.register(CtaProv)
class CtaProv(admin.ModelAdmin):

    
    list_display = ('id','proveedor','fecha','importe_total')

    list_filter=('proveedor','fecha')

    autocomplete_fields = ['proveedor','tipo_cpte','categoria','producto']

