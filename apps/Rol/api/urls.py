
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Rol.api.views import RolViewSet

router_rol = DefaultRouter()
router_rol.register(prefix='rol', basename='rol', viewset=RolViewSet)

