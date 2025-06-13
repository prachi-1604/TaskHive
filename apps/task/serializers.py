from rest_framework import serializers

from apps.task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completion_date', 'file', 'created_by', 'status', 'assigned_to')
        read_only_fields = ['created_by', 'status']
