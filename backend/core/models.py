import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Abstract base model for shared fields and behaviors."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        default_permissions = ("add", "change", "delete", "view")
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"
