from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Ambiente.api.urls import router_ambiente
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

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router_ambiente.urls)),
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
]
