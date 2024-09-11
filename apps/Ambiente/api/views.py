from rest_framework import generics, status
from rest_framework.response import Response
from apps.Ambiente.models import Ambiente
from apps.Ambiente.api.Serializer import AmbienteSerializer

# aqui listo todos mis ambientes con (list) y puedo agregar uno nuevo con (create)
class ListarCrearAmbientes(generics.ListCreateAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

    def list(self, request):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No hay ambientes registrados"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        return super().create(request)

# y aqui el resto de funciones que requieren id
class DetalleActualizarEliminarAmbiente(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Ambiente.DoesNotExist:
            return Response({"message": "Ambiente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Ambiente.DoesNotExist:
            return Response({"message": "Ambiente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Ambiente.DoesNotExist:
            return Response({"message": "Ambiente no encontrado"}, status=status.HTTP_404_NOT_FOUND)