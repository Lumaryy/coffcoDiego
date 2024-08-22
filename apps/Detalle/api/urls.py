from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Detalle.api.views import DetalleViewSet

router_detalle = DefaultRouter()
router_detalle.register(prefix='detalle',basename='detalle', viewset=DetalleViewSet)

