from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Muestra.api.views import MuestraViewSet

router_muestra = DefaultRouter()
router_muestra.register(prefix='muestra', basename='muestra', viewset=MuestraViewSet)
