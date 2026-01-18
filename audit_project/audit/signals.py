from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog, Issue

@receiver(post_save, sender=Issue)
def log_issue_save(sender, instance, created, **kwargs):
    action = "Created" if created else "Updated"

    AuditLog.objects.create(
        user=None,
        action=action,
        model_name="Issue",
        object_id=instance.id
    )


@receiver(post_delete, sender=Issue)
def log_issue_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        user=None,
        action="Deleted",
        model_name="Issue",
        object_id=instance.id
    )
