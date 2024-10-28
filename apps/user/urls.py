# meal URL
from django.urls import include, path
from rest_framework.routers import DefaultRouter # type: ignore
from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  
  ]
