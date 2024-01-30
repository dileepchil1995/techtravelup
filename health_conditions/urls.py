from django.urls import path, include
from rest_framework import routers
from .views import HealthConditionViewSet

router = routers.DefaultRouter()
router.register(r'health-conditions', HealthConditionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
