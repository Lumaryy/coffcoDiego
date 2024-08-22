
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Variables.api.views import  VariableViewSet

router_variables = DefaultRouter()
router_variables.register(prefix='variables', basename='variables', viewset=VariableViewSet)

