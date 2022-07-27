
from django import forms

from cheff_app.models import *
from random import choices


class MesaForm(forms.ModelForm):
    
    capacidad = forms.IntegerField(label='Capacidad', widget=forms.NumberInput(attrs={'placeholder': 'personas'}))
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'placeholder': 'ubicacion'}))
    class Meta:
        model = Mesa
        fields = ('numero', 'capacidad','descripcion')

        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ('codigo','categoria','nombre','precio_costo','precio_venta','un_medida','medida_producto')


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude = ('id',)
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('codigo','nombre')

class Moza_oForm(forms.ModelForm):

    legajo = forms.IntegerField(label='Legajo', widget=forms.NumberInput(attrs={'placeholder': 'legajo'}))
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
        fields = ('id','tipo')

class CtaProvForm(forms.ModelForm):
    class Meta:

        model = CtaProv
        
        exclude = ('id','debe','haber','saldo')
        
