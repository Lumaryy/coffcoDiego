from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Precio.api.views import PrecioViewSet

router_precio = DefaultRouter()
router_precio.register(prefix='precio', basename='precio', viewset=PrecioViewSet)
