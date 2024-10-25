# training/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainingListView.as_view(), name='training_list'),
    path('add/', views.TrainingCreateView.as_view(), name='training_add'),
    path('<int:pk>/', views.TrainingDetailView.as_view(), name='training_detail'),
    path('<int:pk>/edit/', views.TrainingUpdateView.as_view(), name='training_edit'),
    path('<int:pk>/delete/', views.TrainingDeleteView.as_view(), name='training_delete'),
]
