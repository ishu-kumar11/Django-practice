from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Task, SignalLog

@receiver(pre_save, sender=Task)
def before_task_save(sender, instance, **kwargs):
	SignalLog.objects.create(message=f"PRE_SAVE: About to save task'{instance.title}'")

@receiver(post_save, sender=Task)
def after_task_save(sender, instance, created, **kwargs):
	if created:
		SignalLog.objects.create(message=f"POST_SAVE: Task '{instance.title}' was created")
	else:
		SignalLog.objects.create(message=f"POST_SAVE: Task '{instance.title}' was updated")

@receiver(pre_delete, sender=Task)
def before_task_delete(sender, instance, **kwargs):
	SignalLog.objects.create(message=f"PRE_DELETE: About to delete task'{instance.title}'")

@receiver(post_delete, sender=Task)
def after_task_delete(sender, instance, **kwargs):
	SignalLog.objects.create(message=f"POST_DELETE: Task'{instance.title}' deleted")

