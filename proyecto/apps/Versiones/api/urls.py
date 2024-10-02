from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Versiones.api.views import VersionViewSet

router_versiones = DefaultRouter()

router_versiones.register(prefix='versiones', basename='versiones', viewset=VersionViewSet)


