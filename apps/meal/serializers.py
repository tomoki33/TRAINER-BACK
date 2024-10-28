from rest_framework import serializers # type: ignore
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'date', 'meal_type', 'title']  # 必要なフィールドを指定
