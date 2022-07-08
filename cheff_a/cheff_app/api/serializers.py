
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

class InsumosSerializer(serializers.ModelSerializer):

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class meta:
        model = Insumos
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


