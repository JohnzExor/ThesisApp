from django.urls import path
from . import views

app_name = "thesis"
urlpatterns = [
    path("", views.thesis_list, name="thesis_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.thesis_details,
        name="thesis_details",
    ),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path("comment/", views.thesis_search, name="thesis_search")
]
