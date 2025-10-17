from django.db import models

from users.models import CustomUser
from .team import Team


class Project(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "Ac"
        ARCHIVED = "Ar"
        COMPLETED = "C"

    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.ACTIVE
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
