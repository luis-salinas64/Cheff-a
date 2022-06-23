from django import forms
from cheff_app.models import *
from random import choices



class ProductoElaboradoForm(forms.ModelForm):


    codigo = forms.FloatField(label= "Codigo", required=True)
    categoria = forms.ModelChoiceField(label="Categoria", queryset=Categoria.objects.all(),initial=0)
    nombre = forms.CharField(label="Nombre", max_length=20, required=True)
    descripcion = forms.CharField(label="Descripcion", max_length=100)
    imagen = forms.ImageField(label= "Imagen")
    
    ingrediente_base = forms.ModelChoiceField(label="Ingred Base", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_base = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_base = forms.FloatField(label= "Cant.Ing.Base")
    
    ingrediente_2 = forms.ModelChoiceField(label="Ingred 2", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_2 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_2 = forms.FloatField(label= "Cant.Ing.2")

    ingrediente_3 = forms.ModelChoiceField(label="Ingred 3", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_3 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_3 = forms.FloatField(label= "Cant.Ing.3")

    ingrediente_4 = forms.ModelChoiceField(label="Ingred 4", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_4 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_4 = forms.FloatField(label= "Cant.Ing.4")

    ingrediente_5 = forms.ModelChoiceField(label="Ingred 5", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_5 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_5 = forms.FloatField(label= "Cant.Ing.5")

    ingrediente_6 = forms.ModelChoiceField(label="Ingred 6", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_6 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_6 = forms.FloatField(label= "Cant.Ing.6")

    ingrediente_7 = forms.ModelChoiceField(label="Ingred 7", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_7 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_7 = forms.FloatField(label= "Cant.Ing.7")

    ingrediente_8 = forms.ModelChoiceField(label="Ingred 8", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_8 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_8 = forms.FloatField(label= "Cant.Ing.8")

    ingrediente_9 = forms.ModelChoiceField(label="Ingred 9", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_9 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_9 = forms.FloatField(label= "Cant.Ing.9")

    ingrediente_10 = forms.ModelChoiceField(label="Ingred 10", queryset=Ingredientes.objects.all(),initial=0)
    un_medida_10 = forms.ModelChoiceField(label= "Un.Medida", queryset=UnMedida.objects.all(),initial=0)
    cant_ing_10 = forms.FloatField(label= "Cant.Ing.10")

    porcentual_desperdicio = forms.FloatField(label= "Porcentual Desperdicio")


    class Meta:
        model = ProductoElaborado
        fields = ('__all__')
