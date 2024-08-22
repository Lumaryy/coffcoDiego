from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Ambiente.api.views import AmbienteViewSet

router_ambiente = DefaultRouter()
router_ambiente.register(prefix='ambiente', basename='ambiente', viewset=AmbienteViewSet)
