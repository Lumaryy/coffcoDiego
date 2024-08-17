from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VersionViewSet

router = DefaultRouter()

router.register(r'versiones', VersionViewSet)


