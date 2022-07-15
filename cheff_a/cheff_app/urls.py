from django.contrib import admin
from django.urls import path,include
from django.views.generic import base
from django.views.generic.base import View

from cheff_app.views import *

# Librerías para el manejo de sesión.
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

INDEX_LIST = ['index/', 'index/#', '']
INDEX_PATTERNS = [path(x, BaseView.as_view()) for x in INDEX_LIST]


urlpatterns = [

# cheff_app base:
path('base', BaseView.as_view()),

# NOTE: Manejo de sesión:
path('login', auth_views.LoginView.as_view(template_name='cheff_app/bootstrap-login.html', redirect_authenticated_user=True, redirect_field_name='index'), name='login'
         ),

path('logout', auth_views.LogoutView.as_view(next_page='/cheff-app/index', redirect_field_name='index'),
         ),
path('signup', register, name='register'),
path('index', IndexView.as_view(), name='index'),

path('ok', OkCargaView.as_view(), name='ok'),

path('carga_form_me', login_required(register_mesa), name='carga_form_me'),
path('edit_me/<int:numero>',login_required(edit_me), name='edit_me'),
path('delete_me/<int:numero>',login_required(delete_me), name='delete_me'),

path('carga_form_cat', login_required(register_cat), name='carga_form_cat'),
path('edit_cat/<int:codigo>',login_required(edit_cat), name='edit_cat'),
path('delete_cat/<int:codigo>',login_required(delete_cat), name='delete_cat'),

path('carga_form_moz', login_required(register_moz), name='carga_form_moz'),
path('edit_moz/<int:legajo>',login_required(edit_moz), name='edit_moz'),
path('delete_moz/<int:legajo>',login_required(delete_moz), name='delete_moz'),

path('carga_producto',login_required(register_producto), name='carga_producto'),
path('edit_producto/<int:codigo>',login_required(edit_producto), name='edit_producto'),
path('delete_producto/<int:codigo>',login_required(delete_producto), name='delete_producto'),

path('carga_form_prov',login_required(register_prov), name='carga_form_prov'),
path('carga_form_prov/<int:codigo>',login_required(edit_prov), name='edit_prov'),
path('delete_prov/<int:codigo>',login_required(delete_prov), name='delete_prov'),

path('carga_form_unm',login_required(register_unm), name='carga_form_unm'),
path('carga_form_unm/<int:id>',login_required(edit_unm), name='edit_unm'),
path('delete_unm/<int:id>',login_required(delete_unm), name='delete_unm'),

path('carga_form_cpte',login_required(register_cpte), name='carga_form_cpte'),
path('carga_form_cpte/<int:id>',login_required(edit_cpte), name='edit_cpte'),
path('delete_cpte/<int:id>',login_required(delete_cpte), name='delete_cpte'),

path('carga_ctaprov',login_required(register_ctaprov), name='carga_ctaprov'),


path('lista_me',login_required(ListaMesaView.as_view()), name='lista_me'),
path('lista_producto',login_required(ListaProductoView.as_view()), name='lista_producto'),
path('lista_cat',login_required(ListaCatView.as_view()), name='lista_cat'),
path('lista_prov',login_required(ListaProvView.as_view()), name='lista_prov'),
path('lista_moz',login_required(ListaMozView.as_view()), name='lista_moz'),
path('lista_unm',login_required(ListaUnmView.as_view()), name='lista_unm'),
path('lista_cpte',login_required(ListaCpteView.as_view()), name='lista_cpte'),
path('lista_ctaprov',login_required(ListaCtaProvView.as_view()), name='lista_ctaprov'),

path('admin', login_required(AdminView.as_view()), name='admin'),


# NOTE: Ejemplos de Bootstrap HTML:
path('bootstrap-login', BootstrapLoginUserView.as_view(), name='loginbootstrap'),
path('bootstrap-signup', BootstrapSignupView.as_view(), name='signupbootstrap'),

]