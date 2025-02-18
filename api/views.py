from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Location, Variant, LifeExpectancy
from .serializers import LocationSerializer, VariantSerializer, LifeExpectancySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class LifeExpectancyViewSet(viewsets.ModelViewSet):
    queryset = LifeExpectancy.objects.all()
    serializer_class = LifeExpectancySerializer
