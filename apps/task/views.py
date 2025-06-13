from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.task.models import Task
from apps.task.serializers import TaskSerializer
from apps.task.messages import TASK_LIST_FETCHED, TASK_CREATED_SUCCESSFULLY, NOT_ALLOWED, TASK_MARKED_COMPLETED

class TaskCreateListView(generics.GenericAPIView):
    """
    Create a list of tasks for the authenticated user
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(created_by=request.user)
        serializer = self.get_serializer(tasks, many=True)
        return Response({
            "success": True,
            "message": TASK_LIST_FETCHED,
            "data": serializer.data
        })

    def post(self, request):
        data = request.data.copy()
        data['created_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response({
            "success": True,
            "message": TASK_CREATED_SUCCESSFULLY,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

class TaskCompleteView(generics.UpdateAPIView):
    """
    Mark a task as completed for the authenticated user
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.created_by != request.user:
            return Response({"success": False, "message": NOT_ALLOWED}, status=403)
        task.status = "Completed"
        task.save()
        return Response({
            "success": True,
            "message": TASK_MARKED_COMPLETED,
            "data": TaskSerializer(task).data
        })
