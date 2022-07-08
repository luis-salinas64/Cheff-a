from django.contrib import admin
from cheff_app.models import *

@admin.register(Comprobante)
class Comprobante(admin.ModelAdmin):
    
    list_display = ('id','tipo')


@admin.register(Proveedor)
class Proveedor(admin.ModelAdmin):
    list_display = ('id','nombre','cuit','contacto')

    
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(UnMedida)
class UnMedida(admin.ModelAdmin):
    list_display = ('id','un_medida')


@admin.register(Ingredientes)
class Ingredientes(admin.ModelAdmin):
    list_display = ('id','codigo','nombre','un_medida','medida_producto','precio','cantidad','stock')


@admin.register(ProductoTerminado)
class ProductoTerminado(admin.ModelAdmin):
    
    list_display = ('id','codigo','nombre')

     # NOTE: Filtro lateral de elementos:
    list_filter= ('nombre','categoria')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['nombre']

@admin.register(ProductoElaborado)
class ProductoElaborado(admin.ModelAdmin):
    list_display = ('id','codigo','categoria','nombre','imagen')

     # NOTE: Filtro lateral de elementos:
    list_filter= ('nombre','categoria')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['nombre']


@admin.register(Insumos)
class Insumos_Mesa(admin.ModelAdmin):
    list_display = ('nombre','un_medida','precio','cantidad','stock')


@admin.register(Mesa)
class Mesa(admin.ModelAdmin):
    list_display = ('id','numero','capacidad','descripcion')

@admin.register(Moza_o)
class Moza_o(admin.ModelAdmin):
    list_display = ('id','legajo','nombre','fecha_ingreso')

@admin.register(CtaProv)
class CtaProv(admin.ModelAdmin):
    
    list_display = ('id','proveedor','fecha','importe_total')



