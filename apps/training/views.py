from rest_framework import viewsets # type: ignore
from .models import Training
from .serializers import TrainingSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
