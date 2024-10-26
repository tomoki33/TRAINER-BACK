from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter # type: ignore
from apps.training.views import TrainingViewSet

router = DefaultRouter()
router.register(r'', TrainingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('training/', include(router.urls)),  
  ]
