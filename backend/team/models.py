from django.db import models

from users.models import CustomUser


class Team(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified", "-created"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    ROLE_CHOICES = ((1, "MEMBER"), (2, "ADMIN"), (3, "MANAGER"))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=ROLE_CHOICES, default=1)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}|{self.team}| {self.role}"


class Invitation(models.Model):
    class Status(models.TextChoices):
        PENDING = "P"
        ACCEPTED = "A"
        EXPIRED = "E"

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(unique=True)
    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)


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

    def __str__(self):
        return self.name
