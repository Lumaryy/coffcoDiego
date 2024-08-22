from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Logos.api.views import LogoViewSet

router_logos= DefaultRouter()
router_logos.register(prefix='logos', basename='logos', viewset=LogoViewSet)
