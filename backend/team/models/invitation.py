from django.db import models
from django.utils.timezone import now, timedelta
import uuid
from users.models import CustomUser
from .team import Team


class Invitation(models.Model):
    class Status(models.TextChoices):
        PENDING = "P"
        ACCEPTED = "A"
        EXPIRED = "E"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    token = models.CharField(unique=True, default=uuid.uuid4)
    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=now() + timedelta(days=3))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Invitation"
        verbose_name_plural = "Invitations"

    def invite_link(self):
        return f"https://yourapp.com/invite/{self.token}"
