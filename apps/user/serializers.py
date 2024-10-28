## user serializer
from rest_framework import serializers # type: ignore
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'weight', 'height', 'goal', 'title']  # 必要なフィールドを指定
