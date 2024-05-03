from django.urls import path

from apps.task import views

urlpatterns = [
    path("", views.TaskView.as_view(), name="task"),
]