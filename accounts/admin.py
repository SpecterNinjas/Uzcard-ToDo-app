from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'created', 'updated',)
    list_filter = (
        'created',
    )


admin.site.register(TaskModel, TaskAdmin)
