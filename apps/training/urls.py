# training URL
from django.urls import include, path
from rest_framework.routers import DefaultRouter # type: ignore
from .views import TrainingViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet)

urlpatterns = [
    path('', include(router.urls)),  
  ]
