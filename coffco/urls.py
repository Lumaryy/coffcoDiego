from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Ambiente.api.urls import router_ambiente
from apps.cambios.api.urls import router_cambios
from apps.Detalle.api.urls import router_detalle
from apps.Documentos.api.urls import router_documentos
from apps.Finca.api.urls import router_finca
from apps.Logo_documentos.api.urls import router_logoDocumentos
from apps.Logos.api.urls import router_logos
from apps.Muestra.api.urls import router_muestra
from apps.Municipio.api.urls import router_municipio
from apps.Precio.api.urls import router_precio
from apps.Rol.api.urls import router_rol
from apps.Servicio.api.urls import router_servicio
from apps.tipoDocumento.api.urls import router_tipoDocumento
from apps.TipoServicio.api.urls import router_tipoServicio
from apps.Usuarios.api.urls import router_usuarios
from apps.Valor.api.urls import router_valor
from apps.Variables.api.urls import router_variables
from apps.Versiones.api.urls import router_versiones

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router_ambiente.urls)),
    path('api/', include(router_cambios.urls)),
    path('api/', include(router_detalle.urls)),
    path('api/', include(router_documentos.urls)),
    path('api/', include(router_finca.urls)),
    path('api/', include(router_logoDocumentos.urls)),
    path('api/', include(router_logos.urls)),
    path('api/', include(router_muestra.urls)),
    path('api/', include(router_municipio.urls)),
    path('api/', include(router_precio.urls)),
    path('api/', include(router_rol.urls)),
    path('api/', include(router_servicio.urls)),
    path('api/', include(router_tipoDocumento.urls)),
    path('api/', include(router_tipoServicio.urls)),
    path('api/', include(router_usuarios.urls)),
    path('api/', include(router_valor.urls)),
    path('api/', include(router_variables.urls)),
    path('api/', include(router_versiones.urls)),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
