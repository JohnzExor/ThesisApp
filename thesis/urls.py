from django.urls import path
from . import views

urlpatterns = [
    path("thesis/", views.thesis, name="thesis"),
]
