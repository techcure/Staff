from django.contrib.auth.models import User, Group
from .models import *
from .pagination import *

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.exceptions import APIException
from rest_framework.exceptions import NotFound  

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework import viewsets
from rest_framework import status
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.http import JsonResponse
from django.views import View
from App.serializers import (UserSerializer, 
    GroupSerializer, QuestionSerializer, StudSerializer, 
    # StaffSignUpForm, StudentSignUpForm
    )

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from rest_framework import generics
from django.urls import reverse_lazy


# 1) click on python show one blank html page where page name is python_questions.htnl
# 2) in python_questions.htnl add html table where table body shoulldb be blank
# 3) call ajax while onload and call python_queation list api
# 4) and get the response from the api in ajax and append data in table body same like you did for testjob

@api_view(["POST", "GET"])
def Home1(request, format=None, *args, **kwargs):
    if request.method == 'POST':
        print("okay")
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'question-create.html')


@api_view(['GET', 'PUT', 'DELETE'])
def question_op(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def question_put(request, pk, ormat=None, *args, **kwargs):
    if request.method == 'PUT':
        # import pdb;pdb.set_trace()
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisplayStudents(TemplateView):
    template_name = "test_view.html"

    queryset = Stud.objects.all().values()
    serializer_class = StudSerializer

class DisplayPython(TemplateView):
    template_name = "python.html"

    queryset = Question.objects.filter(subj='Python').values()
    serializer_class = QuestionSerializer

class DisplayJquery(TemplateView):
    template_name = "jquery.html"

    queryset = Question.objects.filter(subj='JQuery').values()
    serializer_class = QuestionSerializer


class DisplayHTML(TemplateView):
    template_name = "html-view.html"

    queryset = Question.objects.filter(subj='HTML').values()
    serializer_class = QuestionSerializer

class display_python_que(ListView):
    model = Question


class UpdateQuestion(UpdateView):
    model = Question
    fields= "__all__"
    success_url= "#"


class IndexViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, format=None, *args, **kwargs):
        que_obj = QuestionSerializer.objects.filter(subj='Python')

        serializer = QuestionSerializer(que_obj)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        response = super(IndexViewSet, self).list(request, *args, **kwargs)
        user_obj = Stud.objects.all()
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data, 'user_obj':user_obj})
        return response

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        que_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Stud.objects.all()
    serializer_class = StudSerializer

    def list(self, request, *args, **kwargs):
        response = super(StudentViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data})
        return response

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = StudSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Python ViewSet

"""

class PythonViewSet(viewsets.ModelViewSet):


    queryset = Question.objects.filter(subj = 'Python')
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):

        queryset = Question.objects.filter(subj = 'Python')
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(PythonViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data})

        return response

    def delete(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        que_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
End Python Viewset 
"""

"""
JQuery ViewSet

"""

class JQueryViewSet(viewsets.ModelViewSet):


    queryset = Question.objects.filter(subj = 'JQuery')
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        response = super(JQueryViewSet, self).list(request, *args, **kwargs)

        return response

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
End JQuery Viewset 
"""

"""
HTML ViewSet

"""

class HTMLViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(subj = 'HTML')
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):

        queryset = Question.objects.filter(subj = 'HTML')
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(HTMLViewSet, self).list(request, *args, **kwargs)

        return response

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
End HTML Viewset 
"""

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class StudViewSet(viewsets.ModelViewSet):

    queryset = Stud.objects.all()
    serializer_class = StudSerializer

def getdata(request):
    return JsonResponse({"name": "Oppppp"})

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class QuestionList(APIView):


    def get(self, request, format=None, *args, **kwargs):
        que_obj = QuestionSerializer.objects.all()
        serializer = QuestionSerializer(que_obj)

        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):

    def get_object(self, pk, *args, **kwargs):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        serializer = QuestionSerializer(que_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        serializer = QuestionSerializer(que_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        que_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
