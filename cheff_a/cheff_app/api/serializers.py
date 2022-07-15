
from cheff_app.models import *
from django.contrib.auth.models import User

from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=Categoria.objects.all())

    un_medida = serializers.PrimaryKeyRelatedField(write_only=True,
                queryset=UnMedida.objects.all())

    class Meta:
        model = Producto
        fields = ('codigo','categoria','nombre','precio_costo','precio_venta',
                'un_medida','medida_producto','cantidad','stock','desperdicio')



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


class Moza_oSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moza_o
        fields = ('__all__')


class MesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesa
        fields = ('__all__')

class CtaProvSerializer(serializers.ModelSerializer):

    class Meta:
        model = CtaProv
        fields = ('__all__')


