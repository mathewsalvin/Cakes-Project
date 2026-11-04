from django.db import models
from django.contrib.auth.models import AbstractUser


class RoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'


class Profile(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=RoleChoices.choices,
        default=RoleChoices.USER
    )

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.username