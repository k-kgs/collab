from django.urls import path

from apps.project import views

urlpatterns = [
    path("health", views.HealthCheck.as_view(), name="health"),
    path("list", views.ProjectListView.as_view(), name="project-list"),
    path("", views.HealthCheck.as_view(), name="project"),
]