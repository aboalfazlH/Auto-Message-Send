from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

name = "accounts"

urlpatterns = [
    path("login/",LoginView.as_view(next_page="home-page"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
]