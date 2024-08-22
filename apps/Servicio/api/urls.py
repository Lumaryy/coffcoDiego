from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Servicio.api.views import ServicioViewSet

router_servicio = DefaultRouter()
router_servicio.register(prefix='servicio', basename='servicio', viewset=ServicioViewSet)


