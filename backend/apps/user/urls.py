from django.urls import path

from apps.user import views

urlpatterns = [
    path("health", views.HealthCheck.as_view(), name="health"),
    path("register", views.UserRegistration.as_view(), name="register"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("details", views.UserDetails.as_view(), name="userdetails"),
]