from django.urls import path

# Importamos las API_VIEWS:
from cheff_app.api.api_views import *

urlpatterns = [
    # User APIs:
    
    path('user/login/', LoginUserAPIView.as_view()),

    # CRUD APIs:
    path('prod_get/', GetProductoAPIView.as_view()),
    path('prod_post/', PostProductoAPIView.as_view()),
    path('prod_insert/', ListCreateProductoAPIView.as_view()),
    path('prod_put/', RetrieveUpdateProductoAPIView.as_view()),
    path('prod_destroy/', DestroyProductoAPIView.as_view()),


    path('prod_one_get/<int:pk>/', GetOneProductoAPIView.as_view()),
    
]