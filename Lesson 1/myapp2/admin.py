from django.contrib import admin
from .models import Department, Student, Subject, IDCard

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(IDCard)
