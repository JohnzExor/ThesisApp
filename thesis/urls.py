from django.urls import path
from . import views

app_name = "thesis"
urlpatterns = [
    path("", views.thesis, name="thesis_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.thesis_details,
        name="thesis_details",
    ),
    path("home/", views.landing_page, name="thesis_landing_page"),
]
