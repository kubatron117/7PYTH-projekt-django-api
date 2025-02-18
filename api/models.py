from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=255, db_index=True)
    iso3_code = models.CharField(max_length=3, null=True, blank=True)
    iso2_code = models.CharField(max_length=2, null=True, blank=True)
    loc_type_id = models.IntegerField(null=True, blank=True)
    loc_type_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # odpovídá timestamps
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location


class Variant(models.Model):
    var_id = models.IntegerField()
    variant = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.variant


class LifeExpectancy(models.Model):
    birth_year = models.IntegerField()
    life_expectancy_both = models.FloatField()
    life_expectancy_male = models.FloatField()
    life_expectancy_female = models.FloatField()
    loc_id = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='life_expectancies')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='life_expectancies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['location']),
            models.Index(fields=['variant']),
        ]

    def __str__(self):
        return f"{self.location} - {self.variant} ({self.birth_year})"
