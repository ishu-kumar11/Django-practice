from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"



class Issue(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return self.title


'''
Understand deeply:

user -> who did it

action -> what happened

model_name -> Issue, Post, Complaint

object_id -> which record

timestamp -> when

This IS the audit log
'''