# meal URL
from django.urls import include, path
from rest_framework.routers import DefaultRouter # type: ignore
from .views import MealViewSet

router = DefaultRouter()
router.register(r'', MealViewSet)

urlpatterns = [
    path('', include(router.urls)),  
  ]
