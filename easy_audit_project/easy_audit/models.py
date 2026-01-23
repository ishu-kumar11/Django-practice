from django.db import models
from simple_history.models import HistoricalRecords

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('done', 'Done')
        ],
        default='pending'
    )

    is_deleted = models.BooleanField(default=False)

    history = HistoricalRecords()

    def __str__(self):
        return self.title
