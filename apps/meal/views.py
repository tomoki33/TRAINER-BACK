from rest_framework import viewsets # type: ignore
from .models import Meal
from .serializers import MealSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
