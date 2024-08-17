from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MuestraViewSet

router = DefaultRouter()

router.register(r'muestra', MuestraViewSet)
