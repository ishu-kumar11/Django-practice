from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Resources(models.Model):
	CATEGORY_CHOICES = [
		('notes', 'Notes'),
		('pdf', 'PDF'),
		('code', 'Code'),
		('image', 'Image'),
		('others', 'Others'),
	]

	title = models.CharField(max_length=100)
	des = models.TextField()

	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	file = models.FileField(upload_to='resources/files', null=True, blank=True)
	image = models.ImageField(upload_to='resources/images', null=True, blank=True)

	tags = models.ManyToManyField(Tag, blank=True)

	uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

	is_public = models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add = True)

	uploaded_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title
