from django.urls import path, include

from .views import TripView, TripListView, userLogin, userSuccess, userLogout
from . import views

urlpatterns = [
    path("", TripView.as_view(), name="home"), 
    path("trips/", TripListView.as_view(), name="trips"),
    path("addtrip/", views.index, name="addtrip"),
    path("register/", views.userRegister, name="register"),
    path("login/", views.userLogin, name="login"),
    path("logout/", views.userLogout, name="logout"),
    path("success/", views.userSuccess, name="success")
]
