from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.admin_panel.messages import (NOT_ALLOWED, COMPLETED_TASKS_FETCHED)
from apps.task.models import Task
from apps.task.serializers import TaskSerializer

class AdminCompletedTasksView(generics.ListAPIView):
    """
    Admin view to fetch completed tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(status="Completed")
    
    def list(self, request, *args, **kwargs):
        if request.user.role != "ADMIN":
            return Response({"success": False, "message": NOT_ALLOWED}, status=403)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "success": True,
            "message": COMPLETED_TASKS_FETCHED,
            "data": serializer.data
        })
