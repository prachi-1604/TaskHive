from django.urls import path

from apps.task import views

urlpatterns = [
    path('user/tasks/', views.TaskCreateListView.as_view(), name='user-tasks'),
    path('user/tasks/<int:pk>/complete/', views.TaskCompleteView.as_view(), name='task-complete'),
]
