from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PrecioViewSet

router = DefaultRouter()

router.register(r'precio', PrecioViewSet)
