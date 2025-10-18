from django.db import models

from users.models import CustomUser

from .team import Team


class TeamMember(models.Model):
    ROLE_CHOICES = ((1, "MEMBER"), (2, "ADMIN"), (3, "MANAGER"))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=ROLE_CHOICES, default=1)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-joined_at"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def display_role(self):
        if self.role == 1:
            return "MEMBER"
        elif self.role == 2:
            return "ADMIN"
        else:
            return "MANAGER"

    def __str__(self):
        return f"{self.user}({self.role}) | {self.team}"
