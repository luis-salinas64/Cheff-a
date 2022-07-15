from django import forms
from cheff_app.models import *
from random import choices


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ('numero', 'capacidad','descripcion')

        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ('codigo','categoria','nombre','precio_costo','precio_venta','un_medida','medida_producto','cantidad')


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('codigo','nombre','cuit','direccion','telefono','porc_iva')
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('codigo','nombre')

class Moza_oForm(forms.ModelForm):
    class Meta:
        model = Moza_o
        fields = ('__all__')

class UnMedidaForm(forms.ModelForm):
    class Meta:
        model = UnMedida
        fields = ('__all__')

class CpteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = ('__all__')

class CtaProvForm(forms.ModelForm):
    class Meta:
        model = CtaProv
        fields = ('__all__')