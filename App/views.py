from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from .pagination import *
from django.conf import settings

from django.shortcuts import get_object_or_404
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
import json

from django.http import HttpResponse
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from django.views import View
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from App.serializers import (
    # UserSerializer, 
    # GroupSerializer, 
    QuestionSerializer, StudSerializer, ExaminPointSerializer,
    # StaffSignUpForm, StudentSignUpForm
    )

class ExaminPointViewSet(viewsets.ModelViewSet):

    queryset = ExaminPointt.objects.all()
    serializer_class = ExaminPointSerializer

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None, *args, **kwargs):

        numbers_list = range(1, 20)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = ExaminPointSerializer.objects.filter(subj='Python')

        serializer = ExaminPointSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        response = super(ExaminPointViewSet, self).list(request, *args, **kwargs)
        user_obj = ExaminPointt.objects.all()
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data, 'user_obj':user_obj})
        return response

    def post(self, request):

        dataset = ExaminPointt.objects.create(
            name = Stud.objects.filter(name=request.POST.get('name'))[0],
            question = Question.objects.filter(question=request.POST.get('question'))[0],
            givenpoint = request.POST.get('givenpoint'),
            )

        return JsonResponse({"message": "Good"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        que_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST", "GET"])
def Home1(request, format=None, *args, **kwargs):

    if request.method == 'POST':
        print("okay")
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            # print(serializer.errors)
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
def question_put(request, pk, format=None, *args, **kwargs):
    if request.method == 'PUT':
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisplayResult(TemplateView):
    template_name = "results.html"

    queryset = Stud.objects.all().values()
    serializer_class = StudSerializer

class DisplayStudents(TemplateView):
    template_name = "test_view.html"

    queryset = Stud.objects.all().values()
    serializer_class = StudSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def stu_detail(request, *pk, **kwargs):

#     try:
#         snippet = Stud.objects.all()
#     except Stud.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         stdq = Stud.objects.all()
#         serializer = StudSerializer(stdq, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         print("okay")
#         serializer = StudSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             print(serializer.errors)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return render(request, 'test_view.html')



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Stud.objects.all()
    serializer_class = StudSerializer

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        numbers_list = range(1, 1000)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = StudSerializer.objects.all()

        serializer = StudSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

        queryset = Stud.objects.all()
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(StudentViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data})

        return response

    def delete(self, request, pk, format=None, *args, **kwargs):
        que_obj = self.get_object(pk)
        que_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None, *args, **kwargs):
        if request.method == 'POST':
            serializer = StudSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            if serializer.is_valid():
                serializer.save()
                print(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class DisplayUser(TemplateView):

    template_name = "user-create.html"

    queryset = Stud.objects.all()
    serializer_class = StudSerializer


class display_python_que(ListView):
    model = Question


class UpdateQuestion(UpdateView):
    model = Question
    fields= "__all__"
    success_url= "#"


class IndexViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None, *args, **kwargs):

        numbers_list = range(1, 20)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = QuestionSerializer.objects.filter(subj='Python')

        serializer = QuestionSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
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

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination    

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

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        numbers_list = range(1, 1000)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = QuestionSerializer.objects.filter(subj='Python')

        serializer = QuestionSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

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

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        numbers_list = range(1, 1000)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = QuestionSerializer.objects.filter(subj='JQuery')

        serializer = QuestionSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

        queryset = Question.objects.filter(subj = 'JQuery')
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(JQueryViewSet, self).list(request, *args, **kwargs)
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
End JQuery Viewset 
"""

"""
HTML ViewSet

"""

class HTMLViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(subj = 'HTML')
    serializer_class = QuestionSerializer

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        numbers_list = range(1, 1000)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = QuestionSerializer.objects.filter(subj='HTML')

        serializer = QuestionSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

        queryset = Question.objects.filter(subj = 'HTML')
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(HTMLViewSet, self).list(request, *args, **kwargs)
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
End HTML Viewset 
"""

# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):

#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


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


from django.db.models import Q

@api_view(["POST", "GET"])
def GetData(request, format=None, *args, **kwargs):

    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)

        name=serializer["question"]
        values=serializer["answer"]
        query_to_do = Q()
        if len(name) == len(values):
            for i in range(len(name)):
                query_to_do = query_to_do & Q(output[name[i]]==values[i])