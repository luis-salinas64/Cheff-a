from django.urls import path

# Importamos las API_VIEWS:
from cheff_app.api.api_views import *

urlpatterns = [
    # User APIs:
    
    path('user/login/', LoginUserAPIView.as_view()),

    # CRUD APIs:
    path('ptget/', GetPtAPIView.as_view()),
    path('ptpost/', PostPtAPIView.as_view()),
    path('ptinsert/', ListCreatePtAPIView.as_view()),
    path('ptput/', RetrieveUpdatePtAPIView.as_view()),
    path('ptdestroy/', DestroyPtAPIView.as_view()),


    path('ptget/<int:pk>/', GetOnePtAPIView.as_view()),
    
]