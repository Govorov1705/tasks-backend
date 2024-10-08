from django.urls import path

from . import views


urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view())
]
