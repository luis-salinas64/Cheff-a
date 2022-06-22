from django.contrib import admin
from cheff_app.models import *

@admin.register(Comprobante)
class Comprobante(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(Proveedor)
class Proveedor(admin.ModelAdmin):
    list_display = ('id','nombre','cuit','debe','haber','saldo','contacto')

    
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ('id','nombre')


@admin.register(UnMedida)
class UnMedida(admin.ModelAdmin):
    list_display = ('id','un_medida')


@admin.register(Ingredientes)
class Ingredientes(admin.ModelAdmin):
    list_display = ('id','nombre','un_medida','medida_producto','precio','cantidad','stock')


@admin.register(ProductoTerminado)
class ProductoTerminado(admin.ModelAdmin):
    list_display = ('codigo','categoria','nombre')

     # NOTE: Filtro lateral de elementos:
    list_filter= ('nombre','categoria')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['nombre']

@admin.register(ProductoElaborado)
class ProductoElaborado(admin.ModelAdmin):
    list_display = ('codigo','categoria','nombre')

     # NOTE: Filtro lateral de elementos:
    list_filter= ('nombre','categoria')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['nombre']


@admin.register(Operacion)
class Operacion(admin.ModelAdmin):
    list_display = ('cpte_nro','fecha','producto_terminado','producto_elaborado','ingredientes','precio')


@admin.register(Insumos_Mesa)
class Insumos_Mesa(admin.ModelAdmin):
    list_display = ('nombre','un_medida','precio','cantidad','stock')


@admin.register(Mesa)
class Mesa(admin.ModelAdmin):
    list_display = ('id','numero')

@admin.register(Moza_o)
class Moza_o(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    list_display = ('id','fecha','mesa','moza_o','codigo_pt','cant_pt','codigo_pe','cant_pe','insumo_mesa','importe')