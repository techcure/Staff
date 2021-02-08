from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from django.conf import settings
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import *

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polling
        fields = '__all__'