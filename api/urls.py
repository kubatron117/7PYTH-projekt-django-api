from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, VariantViewSet, LifeExpectancyViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'variants', VariantViewSet)
router.register(r'life-expectancies', LifeExpectancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
