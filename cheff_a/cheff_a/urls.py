from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

from cheff_a.settings import MEDIA_ROOT



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cheff-app/', include('cheff_app.api.urls')),
    path('cheff-app/', include('cheff_app.urls')),

    path('api-docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('openapi', get_schema_view(
        title="Cheff App",
        description='''
</br>
</br>
<h2>Documentación general de APIs de la aplicación Cheff-app</h2>
'''
,
        version="1.0.0"
    ), name='openapi-schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
