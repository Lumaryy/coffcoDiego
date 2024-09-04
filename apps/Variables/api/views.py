from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Variables.models import Variables
from apps.Variables.api.Serializer import VariablesSerializer

class VariableViewSet(viewsets.ViewSet):
    
    def list(self, request):
        """
        List all Variables instances.
        """
        variables = Variables.objects.all()
        serializer = VariablesSerializer(variables, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):

        try:
            variable = Variables.objects.get(pk=pk)
        except Variables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VariablesSerializer(variable)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):

        serializer = VariablesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):

        try:
            variable = Variables.objects.get(pk=pk)
        except Variables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VariablesSerializer(variable, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):

        try:
            variable = Variables.objects.get(pk=pk)
        except Variables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        variable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
