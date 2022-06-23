
from cheff_app.models import *
from django.contrib.auth.models import User

from rest_framework import serializers

class ComprobanteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comprobante
        fields = ('__all__')

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('__all__')

class UnMedidaSerilizer(serializers.ModelSerializer):

    class Meta:
        model = UnMedida
        fields = ('__all__')

class IngredientesSerializer(serializers.ModelSerializer):

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class Meta:
        model = Ingredientes
        fields = ('nombre','precio','un_medida','medida_producto','cantidad','stock')

class Insumos_MesaSerializer(serializers.ModelSerializer):

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class meta:
        model = Insumos_Mesa
        fields = ('nombre','precio','un_medida','medida_producto','cantidad','stock')

class ProductoTerminadoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Categoria.objects.all())

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class Meta:
        model = ProductoTerminado
        fields = ('codigo','categoria','nombre','precio_costo','precio_venta',
                'un_medida','medida_producto','cantidad','stock','desperdicio')

class ProductoElaboradoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Categoria.objects.all())
    
    ingrediente_base = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_2 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_2 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_3 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_3 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_4 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_4 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_5 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_5 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_6 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_6 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_7 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_7 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())
        
    ingrediente_8 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_8 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_9 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_9 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    ingrediente_10 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    un_medida_10 = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class Meta:
        model = ProductoElaborado
        fields =('__all__') 
        #('codigo','categoria','nombre','descripcion','imagen','ingrediente_base','ingrediente_2',
        #        'ingrediente_3','ingrediente_4','ingrediente_5','ingrediente_6','ingrediente_7',
        #        'ingrediente_8','ingrediente_9','ingrediente_10','porcentual_desperdicio')

class Moza_oSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moza_o
        fields = ('__all__')

class MesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesa
        fields = ('__all__')

class OperacionSerializer(serializers.ModelSerializer):

    moza_o = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Moza_o.objects.all())

    tipo = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Comprobante.objects.all())

    proveedor = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Proveedor.objects.all())

    categoria = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Categoria.objects.all())

    producto_terminado = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=ProductoTerminado.objects.all())

    producto_elaborado = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=ProductoElaborado.objects.all())

    ingredientes = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Ingredientes.objects.all())

    

    class Meta:
        model = Operacion
        fields = ('cpte_nro','moza_o','fecha','tipo','proveedor','categoria','producto_terminado',
                'producto_elaborado','ingredientes','precio','cantidad','importe')

class TicketSerializer(serializers.ModelSerializer):

    mesa = serializers.PrimaryKeyRelatedField(write_only=True,
            queryset=Mesa.objects.all())

    moza_o = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Moza_o.objects.all())

    codigo_pt = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=ProductoTerminado.objects.all())

    codigo_pe = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=ProductoElaborado.objects.all())

    insumo_mesa = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Insumos_Mesa.objects.all())


    class Meta:
        model = Ticket
        fields = ('fecha','mesa','moza_o','codigo_pt','cant_pt','codigo_pe','cant_pe',
                'insumo_mesa','importe')



