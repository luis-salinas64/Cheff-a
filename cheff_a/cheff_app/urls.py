from django.contrib import admin
from django.urls import path,include
from django.views.generic import base
from django.views.generic.base import View

from cheff_app.views import *

# Librerías para el manejo de sesión.
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

INDEX_LIST = ['base/', 'base/#', '']
INDEX_PATTERNS = [path(x, BaseView.as_view()) for x in INDEX_LIST]


urlpatterns = [

# cheff_app base:
path('base', BaseView.as_view()),

# NOTE: Manejo de sesión:
path('login', auth_views.LoginView.as_view(template_name='cheff_app/bootstrap-login.html', redirect_authenticated_user=True, redirect_field_name='base'), name='login'
         ),

path('logout', auth_views.LogoutView.as_view(next_page='/cheff_app/base', redirect_field_name='base'),
         ),
path('signup', register, name='register'),


]