from django.urls import path

from apps.admin_panel import views


urlpatterns = [
    path('admin/completed-tasks/', views.AdminCompletedTasksView.as_view(), name='admin-tasks'),
]
