from django.urls import path
from django.contrib.auth import login, logout
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("create/", views.Create_Account.as_view(), name="create"),
    path("login/", views.Account_login.as_view(), name="login"),
    path("logout/", views.Account_logout.as_view(), name='logout'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
]