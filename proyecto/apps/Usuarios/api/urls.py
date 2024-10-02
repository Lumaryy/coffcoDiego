
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Usuarios.api.views import UsuarioViewSet


router_usuarios = DefaultRouter()

router_usuarios.register(prefix='ambiente', basename='ambiente', viewset=UsuarioViewSet)





