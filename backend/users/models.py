from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    portfolio_link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.super()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
