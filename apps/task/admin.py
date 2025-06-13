from django.contrib import admin
from apps.task.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_by', 'assigned_to', 'completion_date')
    list_filter = ('status', 'completion_date')
    search_fields = ('title', 'description')
    autocomplete_fields = ('created_by', 'assigned_to')
    date_hierarchy = 'completion_date'
    ordering = ('-created_at',)
