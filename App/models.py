from django.conf import settings
from django.db import models
from django.utils import timezone


class Stud(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Question(models.Model):

    SUB = (
    ('Python','Python'),
    ('JQuery', 'JQuery'),
    ('JavaScript','JavaScript'),)

    QUETYPE = (
    ('Easy','Easy'),
    ('Medium', 'Medium'),
    ('Hard','Hard'),)

    question = models.CharField(max_length=200)
    subj = models.CharField(max_length=10, choices=SUB, default='Python')
    answer = models.TextField(max_length=200, null = True, blank = True)
    quetype = models.CharField(max_length=10, choices=QUETYPE, default='Easy')


    def __str__(self):
        return str(self.question)