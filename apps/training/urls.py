from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import TrainingViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
