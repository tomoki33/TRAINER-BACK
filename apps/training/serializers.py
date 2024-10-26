from rest_framework import serializers # type: ignore
from .models import Training

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'title', 'description']  # 必要なフィールドを指定
