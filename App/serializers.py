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

from .models import (User)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def get_ques(self, obj):
        queryset = Question.objects.filter(owner=obj)
        Question = QuestionSerializer(queryset, many=True, context=self.context).data
        return Question

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question',instance.question)
        instance.answer = validated_data.get('answer',instance.answer)
        instance.subj = validated_data.get('subj',instance.subj)
        instance.quetype = validated_data.get('quetype',instance.quetype)
        instance.point = validated_data.get('point',instance.point)

        instance.save()
        return instance

    def create(self, validated_data):
        print(validated_data)
        return Question.objects.create(**validated_data)


class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stud
        fields = '__all__'

    def get(self, *obj):
        queryset = Stud.objects.all()
        std = StudSerializer(queryset, many=True, context=self.context).data
        return Question

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

    def create(self, validated_data):
        print(validated_data)
        return Stud.objects.create(**validated_data)


class ExaminPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminPoint
        fields = '__all__'

    def get(self, *obj):
        queryset = ExaminPoint.objects.all()
        std = ExaminPointSerializer(queryset, many=True, context=self.context).data
        return Question

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

    def create(self, validated_data):
        print(validated_data)
        return ExaminPoint.objects.create(**validated_data)
