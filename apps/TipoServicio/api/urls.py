
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.TipoServicio.api.views import TipoServicioViewSet

router_tipoServicio= DefaultRouter()
router_tipoServicio.register(prefix='tipoServicio', basename='tipoServicio', viewset=TipoServicioViewSet)
