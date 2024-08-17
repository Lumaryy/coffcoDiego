
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  VariableViewSet

router = DefaultRouter()

router.register(r'variables', VariableViewSet)

