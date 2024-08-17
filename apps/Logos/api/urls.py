from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LogoViewSet

router = DefaultRouter()

router.register(r'logos', LogoViewSet)
