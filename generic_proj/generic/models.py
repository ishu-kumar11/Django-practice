from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Post(models.Model):
	title = models.CharField(max_length=50)

	comments = GenericRelation('Comment')

	def __str__(self):
		return self.title


class Photo(models.Model):
	caption = models.CharField(max_length=100)

	comments = GenericRelation('Comment')

	def __str__(self):
		return self.caption

class Comment(models.Model):
    text = models.CharField(max_length=200)

    # Generic Relation Fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text



