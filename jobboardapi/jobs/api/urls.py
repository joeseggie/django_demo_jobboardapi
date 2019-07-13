from django.urls import path

from .views import JobDetailApiView
from .views import JobListCreateAPIView


urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailApiView.as_view(), name='job-detail'),
]
