from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

from django.db.models.signals import post_save
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Stud(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)

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

    question = models.CharField(max_length=200, default=None, blank=True,null=True)
    subj = models.CharField(max_length=10, choices=SUB, default='Python')
    answer = models.TextField(max_length=200, null = True, blank = True)
    quetype = models.CharField(max_length=10, choices=QUETYPE, default='Easy')
    point = models.CharField(max_length=200, null = True, blank = True)


    def __str__(self):
        template = '{0.subj} {0.question} {0.subj} {0.answer} {0.quetype}'
        return template.format(self)

class ExaminPointt(models.Model):

    name = models.ForeignKey(Stud, on_delete=models.CASCADE, blank=True,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True,null=True)
    givenpoint = models.CharField(max_length=200, null = True, blank = True)
    
    class Meta:
        unique_together = ['name', 'question']
        ordering = ['name']


    def __str__(self):
        template = '{0.name}'
        return template.format(self)