from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import AmbienteViewSet

router = DefaultRouter()

router.register(r'ambiente', AmbienteViewSet)