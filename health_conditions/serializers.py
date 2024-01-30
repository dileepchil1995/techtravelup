from rest_framework import serializers
from .models import HealthCondition

class HealthConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCondition
        fields = '__all__'
