from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from django.conf import settings
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

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
        Question = CitySerializer(queryset, many=True, context=self.context).data
        return Question

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question',instance.question)
        instance.subj = validated_data.get('subj',instance.subj)

        instance.save()
        return instance

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stud
        fields = '__all__'