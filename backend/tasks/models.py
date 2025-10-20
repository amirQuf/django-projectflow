from django.db import models
from team.models.project import Project
from users.models import CustomUser
from django.utils import timezone


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "L"
        MEDIUM = "M"
        HIGHT = "H"
        URGENT = "U"

    class Status(models.TextChoices):
        TODO = "T"
        IN_PROGRESS = "P"
        DONE = "D"

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=1, choices=Priority.choices, default=Priority.LOW
    )
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.TODO)

    due_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title


class Comment(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
