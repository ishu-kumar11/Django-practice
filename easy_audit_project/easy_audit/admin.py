from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Task

@admin.register(Task)
class TaskAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'status')
