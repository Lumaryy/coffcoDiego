
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TipoServicioViewSet

router = DefaultRouter()

router.register(r'tiposervicio', TipoServicioViewSet)


