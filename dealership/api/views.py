from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from inventory.models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer