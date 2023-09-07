from django.urls import path
from django.contrib.auth import login, logout
from . import views

app_name = "discord_list"
urlpatterns = [
    path("", views.home, name="index"),
]