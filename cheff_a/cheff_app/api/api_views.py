from cheff_app.api.serializers import *
from cheff_app.models import *
from django.contrib.auth.models import User

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView)

# Importamos librerías para gestionar los permisos de acceso a nuestras APIs

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


class LoginUserAPIView(APIView):
    '''
    Vista de API personalizada para recibir peticiones de tipo POST.
    Esquema de entrada:
    {"username":"root", "password":12345}
    
    Utilizaremos JSONParser para tener  'Content-Type': 'application/json'
    '''
    parser_classes = [JSONParser]
    authentication_classes = []
    permission_classes = []

    def post(self, request,format=None):
        '''
        Esta función sobrescribe la función post original de esta clase,
        recibe "request" y hay que setear format=None, para poder recibir los datos en request.data 
        la idea es obtener los datos enviados en el request y autenticar al usuario con la 
        función "authenticate()", la cual devuelve el estado de autenticación.
        \nLuego con estos datos se consulta el Token generado para el usuario, si no lo tiene asignado,
        se crea automáticamente.
        \nEsquema de entrada:
        \n`{"username":"root", "password":12345}`
        \nUtilizaremos JSONParser para tener  `'Content-Type': 'application/json'`
        '''
        user_data = {}
        try:
            # Obtenemos los datos del request:
            username = request.data.get('username')
            password = request.data.get('password')
            # Obtenemos el objeto del modelo user, a partir del usuario y contraseña,
            # NOTE: es importante el uso de este método, porque aplica el hash del password!
            account = authenticate(username=username, password=password)

            if account:
                # Si el usuario existe y sus credenciales son validas, tratamos de obtener el TOKEN:
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    # Si el TOKEN del usuario no existe, lo creamos automáticamente:
                    token = Token.objects.create(user=account)
                # Con todos estos datos, construimos un JSON de respuesta:
                user_data['user_id'] = account.pk
                user_data['username'] = username
                user_data['first_name'] = account.first_name
                user_data['last_name'] = account.first_name
                user_data['email']=account.email
                user_data['is_active'] = account.is_active
                user_data['token'] = token.key                
                # Devolvemos la respuesta personalizada
                return Response(user_data)
            else:
                # Si las credenciales son invalidas, devolvemos algun mensaje de error:
                user_data['response'] = 'Error'
                user_data['error_message'] = 'Credenciales invalidas'
                return Response(user_data)

        except Exception as error:
            # Si aparece alguna excepción, devolvemos un mensaje de error
            user_data['response'] = 'Error'
            user_data['error_message'] = error
            return Response(user_data)


class GetProductoAPIView(ListAPIView):
    __doc__ = f'''{'GET'} 
    `[METODO GET]`
    Esta vista de API nos devuelve una lista de todos los productos presentes 
    en la base de datos.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



class PostProductoAPIView(CreateAPIView):
    __doc__ = f'''{''}
    `[METODO POST]`
    Esta vista de API nos permite hacer un insert en la tabla Producto.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ListCreateProductoAPIView(ListCreateAPIView):
    __doc__ = f'''{''}
    `[METODO GET-POST]`
    Esta vista de API nos devuelve una lista de todos los productos presentes 
    en la base de datos.
    Tambien nos permite hacer un insert en la base de datos.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class RetrieveUpdateProductoAPIView(RetrieveUpdateAPIView):
    __doc__ = f'''{''}
    `[METODO GET-PUT-PATCH]`
    Esta vista de API nos permite actualizar un registro, o simplemente visualizarlo.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class DestroyProductoAPIView(DestroyAPIView):
    __doc__ = f'''{''}
    `[METODO DELETE]`
    Esta vista de API nos permite eliminar un registro.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# NOTE: APIs MIXTAS:

class GetOneProductoAPIView(ListAPIView):
    __doc__ = f'''{''}
    `[METODO GET]`
    Esta vista de API nos devuelve un producto en particular de la base de datos.
    '''
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        '''
        Sobrescribimos la función `get_queryset` para poder filtrar el request 
        por medio de la url. En este caso traemos de la url por medio de `self.kwargs` 
        el parámetro id y con él realizamos una query para traer 
        el Producto del ID solicitado.  
        '''
        try:
            producto_id = self.kwargs['id']
            queryset = Producto.objects.filter(id=producto_id)
            return queryset
        except Exception as error:
            return {'error': f'Ha ocurrido la siguiente excepción: {error}'}
