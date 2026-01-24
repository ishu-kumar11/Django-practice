from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title


class SignalLog(models.Model):
	message = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message