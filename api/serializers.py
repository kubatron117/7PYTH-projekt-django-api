from rest_framework import serializers
from .models import Location, Variant, LifeExpectancy

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class LifeExpectancySerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    variant = VariantSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(
        queryset=Variant.objects.all(), source='variant', write_only=True)

    class Meta:
        model = LifeExpectancy
        fields = [
            'id',
            'birth_year',
            'life_expectancy_both',
            'life_expectancy_male',
            'life_expectancy_female',
            'location',
            'variant',
            'location_id',
            'variant_id',
            'created_at',
            'updated_at',
        ]
