from rest_framework import generics, viewsets
from accounts.api import serializers
from accounts.models import User


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = serializers.UsuarioSerializer