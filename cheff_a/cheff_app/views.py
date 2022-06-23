
from django.http import HttpResponse, HttpResponseRedirect


# Importo vistas genericas:
from django.db.models.query import QuerySet
from django.db.models import Count

# from django.db import filters
from django.views.generic import TemplateView, ListView, CreateView,DeleteView,UpdateView
import io

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from cheff_app.models import *


# Formulario de registro:
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from cheff_app.forms import *


class LoginUserView(TemplateView):
    '''
    Formulario de inicio de sesión.
    '''
    template_name = 'cheff_app/login.html'


class UserForm(UserCreationForm):
    '''
    Formulario de creación de usuario.
    Utilizamos un formulario que viene por defecto en Django y que cumple con todos los
    requisitos para agregar un nuevo usuario a la base de datos.
    También tiene los métodos para validar todos sus campos.
    '''
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()



    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')


def register(request):
    '''
    Función que complementa el formulario de registro de usuario.
    Al completar el formulario, se envía la información a esta función que espera
    una petición de tipo `POST`, si la información enviada no es valida o la petición no es POST,
    se redirige nuevamente a la página de registro. Si el registro fue exitoso,
    el usuario será redirigido a la página de logueo.
    '''
    if request.method == 'POST':
        # Si la petición es de tipo POST, analizamos los datos del formulario:
        # Creamos un objeto de tipo UserForm (la clase que creamos mas arriba)
        # Pasandole los datos del request:
        form = UserForm(request.POST)
        # Luego, utilizamos el método que viene en en la clase UserCreationForm
        # para validar los datos del formulario:
        [print('',item) for item in form] # NOTE: Imprimimos para ver el contenido del formulario COMPLETO
        if form.is_valid():
            # Si los datos son validos, el formulario guarda los datos en la base de datos.
            # Al heredar de UserCreationForm, aplica las codificaciónes en el password y todo
            # lo necesario:
            form.save()
            # Con todo terminado, redirigimos a la página de inicio de sesión,
            # porque por defecto, registrar un usuario no es iniciar una sesión.
            return redirect('/cheff_app/bootstrap-login')
    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = UserForm()
    # Si los datos del POST son invalidos o si el método es distinto a POST
    # retornamos el render de la página de registro, con el formulario de registro en el contexto.
    [print('',item) for item in form] # NOTE: Imprimimos para ver el contenido del formulario vacío
    return render(request, 'cheff_app/bootstrap-signup.html', {'form': form})



class BaseView(TemplateView):
    
    template_name = 'cheff_app/base.html'





