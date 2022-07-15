
from django.http import HttpResponse, HttpResponseRedirect


# Importo vistas genericas:
from django.db.models.query import QuerySet
from django.db.models import Count

# from django.db import filters
from django.views.generic import TemplateView, ListView, CreateView,DeleteView,UpdateView
import io
from django.contrib import messages

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from cheff_app.models import *


# Formulario de registro:
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from cheff_app.forms import *

# ----------------------------------Usuarios----------------------------------
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


class IndexView(ListView):
    '''
    Página principal del sitio.
    Utilizamos `ListView` para poder aprovechar sus funciones de paginado.
    Para ello tenemos que utilizar sus atributos:
    \n
    '''
    queryset = Mesa.objects.all().order_by('id')
    # NOTE: Este queryset incorporará una lista de elementos a la que le asignará
    # Automáticamente el nombre de comic_list
    template_name = 'cheff_app/index.html'
    paginate_by = 10

    # NOTE: Examinamos qué incluye nuestro contexto:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
# --------------------------------------- admin ---------------------------------------

class AdminView(TemplateView):
    '''
    Página de administración.
    '''
    template_name = 'cheff_app/admin.html'

# Registrar nueva Mesa:

def register_mesa(request):
    
    form = None

    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')
    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = MesaForm()

    return render(request,'cheff_app/adminer/carga_form_me.html', {'form':form})
            

# Editar Mesa:
def edit_me(request,numero):
    form = None

    mesa = Mesa.objects.get(numero=numero)

    if request.method == 'GET':
        form = MesaForm(instance=mesa)

    else:
        form = MesaForm(request.POST,instance=mesa)


        if form.is_valid():
            form.save()

            return redirect('/cheff-app/ok')
    return render (request, 'cheff_app/adminer/carga_form_me.html', {'form':form})

# Eliminar Mesa

def delete_me(request,numero):

    mesa = Mesa.objects.get(numero=numero)

    if request.method == 'POST':
        mesa.delete()

        return redirect('/cheff-app/lista_me')

    return render(request, 'cheff_app/adminer/delete_me.html', {'mesa':mesa})

# Registrar nueva Categoria:

def register_cat(request):

    form = None

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')
    else:
        form = CategoriaForm()

    return render(request,'cheff_app/adminer/carga_form_cat.html', {'form':form})

# Editar Categoria:

def edit_cat(request,codigo):

    form = None

    categoria = Categoria.objects.get(codigo=codigo)

    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)

    else:
        form = CategoriaForm(request.POST,instance=categoria)

        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')

    return render (request, 'cheff_app/adminer/carga_form_cat.html', {'form':form})

# Eliminar Categoria:

def delete_cat(request,codigo):

    categoria = Categoria.objects.get(codigo=codigo)

    if request.method == 'POST':
        categoria.delete()
        print('Categoria eliminada')

        return redirect('/cheff-app/lista_cat')
    
    return render(request,'cheff_app/adminer/delete_cat.html', {'categoria':categoria})


def register_moz(request):

    form = None

    if request.method == 'POST':

        form = Moza_oForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')
    else:
        form = Moza_oForm()

    return render(request,'cheff_app/adminer/carga_form_moz.html', {'form':form})

# Editar Moza_o:

def edit_moz(request,legajo):

    form = None

    moz = Moza_o.objects.get(legajo=legajo)

    if request.method == 'GET':
        form = Moza_oForm(instance=moz)

    else:
        form = Moza_oForm(request.POST,instance=moz)

        if form.is_valid():
            form.save()
            

            return redirect('/cheff-app/ok')
    return render (request, 'cheff_app/adminer/carga_form_moz.html', {'form':form})

# Eliminar Moza_o:

def delete_moz(request,legajo):

    moz = Moza_o.objects.get(legajo=legajo)

    if request.method == 'POST':
        moz.delete()
        
        return redirect('/cheff-app/lista_moz')
    
    return render(request,'cheff_app/adminer/delete_moz.html', {'moz':moz})



# Registrar nuevo Producto :
def register_producto(request):
    
    if request.method == 'POST':
        
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("valido")

            return redirect('/cheff-app/ok')

    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = ProductoForm()

    return render(request,'cheff_app/adminer/carga_producto.html', {'form':form})

# Editar Producto:
def edit_producto(request,codigo):
    form = None

    producto = Producto.objects.get(codigo=codigo)

    if request.method == 'GET':
        form = ProductoForm(instance=producto)

    else:
        form = ProductoForm(request.POST,instance=producto)

        if form.is_valid():
            form.save()

            return redirect('/cheff-app/ok')

    return render (request, 'cheff_app/adminer/carga_producto.html', {'form':form})

# Borrar Producto

def delete_producto (request,codigo):

    pe = Producto.objects.get(codigo=codigo)
    if request.method=="POST":

        pe.delete()
        return redirect('/cheff-app/lista_producto')

    return render(request,'cheff_app/adminer/delete_producto.html',{'pe':pe})

# Registrar nuevo Proveedor:
def register_prov(request):
    
    if request.method == 'POST':
        
        form = ProveedorForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("valido")

            return redirect('/cheff-app/ok')

    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = ProveedorForm()

    return render(request,'cheff_app/adminer/carga_form_prov.html', {'form':form})

# Editar Proveedor:
def edit_prov(request,codigo):
    form = None

    proveedor = Proveedor.objects.get(codigo=codigo)

    if request.method == 'GET':
        form = ProveedorForm(instance=proveedor)

    else:
        form = ProveedorForm(request.POST,instance=proveedor)

        if form.is_valid():
            form.save()
            

            return redirect('/cheff-app/ok')

    return render (request, 'cheff_app/adminer/carga_form_prov.html', {'form':form})

# Borrar Proveedor:
def delete_prov(request,codigo):
    form = None

    proveedor = Proveedor.objects.get(codigo=codigo)

    if request.method == 'POST':
        proveedor.delete()
        
        return redirect('/cheff-app/lista_prov')

    return render(request,'cheff_app/adminer/delete_prov.html',{'proveedor':proveedor})

# Registrar nueva Unidad de Medida:
def register_unm(request):
    form = None

    if request.method == 'POST':
        form = UnMedidaForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')
    
    else:
        
        form = UnMedidaForm()

    return render(request,'cheff_app/adminer/carga_form_unm.html', {'form':form})

# Editar Unidad de Medida:
def edit_unm(request,id):
    form = None

    unidad = UnMedida.objects.get(id=id)

    if request.method == 'GET':
        form = UnMedidaForm(instance=unidad)

    else:
        form = UnMedidaForm(request.POST,instance=unidad)

        if form.is_valid():
            form.save()
            
            return redirect('/cheff-app/ok')

    return render (request, 'cheff_app/adminer/carga_form_unm.html', {'form':form})

def delete_unm(request,id):
    form = None

    unidad = UnMedida.objects.get(id=id)

    if request.method == 'POST':
        
        unidad.delete()
        
        return redirect('/cheff-app/lista_unm')

    return render(request,'cheff_app/adminer/delete_unm.html',{'unidad':unidad})


# Registrar nuevo Comprobante:
def register_cpte(request):
    form = None

    if request.method == 'POST':
        form = CpteForm(request.POST)

        if form.is_valid():
            form.save()
            print("valido")

            return redirect('/cheff-app/ok')
    
    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = CpteForm()

    return render(request,'cheff_app/adminer/carga_form_cpte.html', {'form':form})

# Editar Comprobante:
def edit_cpte(request,id):
    form = None

    cpte = Comprobante.objects.get(id=id)

    if request.method == 'GET':
        form = CpteForm(instance=cpte)

    else:
        form = CpteForm(request.POST,instance=cpte)

        if form.is_valid():
            form.save()

            return redirect('/cheff-app/ok')

    return render (request, 'cheff_app/adminer/carga_form_cpte.html', {'form':form})

# Eliminar Comprobante:
def delete_cpte(request,id):
    form = None
    
    cpte = Comprobante.objects.get(id=id)

    if request.method == 'POST':
        
        cpte.delete()
        
        return redirect('/cheff-app/lista_cpte')

    return render(request,'cheff_app/adminer/delete_cpte.html',{'cpte':cpte})


# Confirmacion de carga correcta
class OkCargaView(TemplateView):
    template_name = 'cheff_app/ok.html'



# Registrar cuenta Proveedor:

def register_ctaprov(request):
    
    form = None

    if request.method == 'POST':
        form = CtaProvForm(request.POST)

        if form.is_valid():
            form.save()
            print("valido")

            return redirect('/cheff-app/ok')
    
    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización.
        form = CtaProvForm()

    return render(request,'cheff_app/adminer/carga_ctaprov.html', {'form':form})

# ------------------------------ listados ----------------------------------------

class ListaProductoView(ListView):
    '''
    Página de listado de Productos.
    '''
    queryset = Producto.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_producto.html'
    paginate_by = 10


class ListaMesaView(ListView):
    '''
    Página de listado de Mesas.
    '''
    queryset = Mesa.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_me.html'
    paginate_by = 10

class ListaCatView(ListView):
    '''
    Página de listado de Categorias.
    '''
    queryset = Categoria.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_cat.html'
    paginate_by = 10

class ListaProvView(ListView):
    '''
    Página de listado de Proveedores.
    '''
    queryset = Proveedor.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_prov.html'
    paginate_by = 10

class ListaMozView(ListView):
    '''
    Página de listado de Mozos.
    '''
    queryset = Moza_o.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_moz.html'
    paginate_by = 10
    
class ListaUnmView(ListView):
    '''
    Página de listado de Unidades de Medida.
    '''
    queryset = UnMedida.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_unm.html'
    paginate_by = 10

class ListaCpteView(ListView):
    '''
    Página de listado de Cptes.
    '''
    queryset = Comprobante.objects.all().order_by('id')
    template_name = 'cheff_app/adminer/lista_cpte.html'
    paginate_by = 10

class ListaCtaProvView(ListView):
    '''
    Página de listado de Cuentas Proveedor.
    '''
    queryset = CtaProv.objects.all().order_by('proveedor')
    template_name = 'cheff_app/adminer/lista_cta_prov.html'
    paginate_by = 10

class DetailView(TemplateView):
    template_name = 'cheff_app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesa'] = Mesa.objects.get(id=kwargs['pk'])


        return context













# NOTE: Vistas con Bootstrap:

class BootstrapLoginUserView(TemplateView):

   # Vista para Template de login con estilo de bootstrap.

    template_name = 'cheff_app/bootstrap-login.html'

class BootstrapSignupView(TemplateView):

    # Vista para Template de registro de usuario con estilo de bootstrap.

    template_name = 'cheff_app/bootstrap-signup.html'