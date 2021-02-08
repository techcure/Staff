from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse


class Polling(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return self.name