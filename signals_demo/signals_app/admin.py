from django.contrib import admin
from .models import Task, SignalLog

admin.site.register(Task)
admin.site.register(SignalLog)
