## config URL
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('training/', include('apps.training.urls')),
    path('meal/', include('apps.meal.urls')),
    path('user/', include('apps.user.urls')),
  ]
