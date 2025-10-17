import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Abstract base model for shared fields and behaviors."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # مهم! تا ازش مدل واقعی در دیتابیس ساخته نشه
        ordering = ["-created_at"]  # به طور پیش‌فرض مرتب‌سازی نزولی بر اساس زمان ساخت
        get_latest_by = "created_at"  # برای latest()
        default_permissions = ("add", "change", "delete", "view")  # دسترسی‌های پیش‌فرض
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"
