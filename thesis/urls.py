from django.urls import path
from . import views

urlpatterns = [
    path("thesis/", views.thesis, name="thesis"),
    path("thesis/<int:id>/", views.thesis_details, name="thesis_details"),
    path("home/", views.landing_page, name="landing_page"),
]
