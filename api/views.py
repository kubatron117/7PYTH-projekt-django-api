from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Location, Variant, LifeExpectancy
from .serializers import LocationSerializer, VariantSerializer, LifeExpectancySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['location', 'iso3_code', 'iso2_code', 'loc_type_name']
    ordering_fields = ['location', 'created_at']


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class LifeExpectancyViewSet(viewsets.ModelViewSet):
    queryset = LifeExpectancy.objects.all()
    serializer_class = LifeExpectancySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['birth_year', 'life_expectancy_both', 'life_expectancy_male', 'life_expectancy_female', 'location']
    ordering_fields = ['location', 'created_at', 'birth_year']
