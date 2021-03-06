from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from pets import serializers
from .models import Pet

# class PetsViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.PetSerializer
#     queryset = Pet.objects.all()

class PetList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()
    serializer_class = serializers.PetSerializer


class PetCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()
    serializer_class = serializers.PetSerializer


class PetUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()
    serializer_class = serializers.PetSerializer

