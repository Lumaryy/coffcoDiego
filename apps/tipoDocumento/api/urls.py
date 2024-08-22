from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tipoDocumento.api.views import TipoDocumentoViewSet

router_tipoDocumento = DefaultRouter()
router_tipoDocumento.register(prefix='tipoDocumento', basename='tipoDocumento', viewset=TipoDocumentoViewSet)

