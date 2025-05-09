from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("team/<int:team_id>/", views.team_detail, name="team_detail"),
]