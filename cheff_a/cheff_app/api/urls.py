from django.urls import path

# Importamos las API_VIEWS:
from cheff_app.api.api_views import *

urlpatterns = [
    # User APIs:
    
    path('user/login/', LoginUserAPIView.as_view()),

    # CRUD APIs:
    path('ptget/', GetPtAPIView.as_view()),
    
]