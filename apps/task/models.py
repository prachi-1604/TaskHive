from django.db import models

from apps.system.models import BaseModel
from apps.task.constant import STATUS_CHOICES
from apps.users.models import User

class Task(BaseModel):
    """
    Task model with fields for title, description, completion date, file, created by, assigned to, and status.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_date = models.DateField()
    file = models.FileField(upload_to='tasks/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title
