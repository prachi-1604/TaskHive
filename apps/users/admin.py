from django.contrib import admin

from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role', 'country', 'is_active')
    list_filter = ('role', 'country', 'is_active')
    search_fields = ('name', 'email')
    ordering = ('id',)
