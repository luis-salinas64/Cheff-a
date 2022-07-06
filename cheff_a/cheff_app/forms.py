from django import forms
from cheff_app.models import *
from random import choices


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ('numero', 'capacidad','descripcion')

class ProductoElaboradoForm(forms.ModelForm):
    class Meta:
        model = ProductoElaborado
        fields = ('__all__')
        
class ProductoTerminadoForm(forms.ModelForm):
    
    class Meta:
        model = ProductoTerminado
        fields = ('codigo','categoria','nombre','precio_costo','precio_venta','un_medida','medida_producto','cantidad')

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingredientes
        fields = ('codigo','nombre','precio','un_medida','medida_producto','cantidad')

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('codigo','nombre','cuit','direccion','contacto')
        
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('__all__')

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