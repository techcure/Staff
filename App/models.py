from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse


# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

class Stud(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):

    SUB = (
    ('Python','Python'),
    ('JQuery', 'JQuery'),
    ('HTML','HTML'),)

    QUETYPE = (
    ('Easy','Easy'),
    ('Medium', 'Medium'),
    ('Hard','Hard'),)

    question = models.CharField(max_length=200)
    subj = models.CharField(max_length=10, choices=SUB, default='Python')
    answer = models.TextField(max_length=200, null = True, blank = True)
    quetype = models.CharField(max_length=10, choices=QUETYPE, default='Easy')
    point = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return str(self.subj)