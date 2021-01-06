from django.contrib.auth.models import User, Group
from .models import *

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from App.serializers import UserSerializer, GroupSerializer, QuestionSerializer, StudSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.views import View


def index_create(request):
    return render(request, 'question-create.html', {})

def index_view(request):

    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.POST)
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            serializer.save()

        return JsonResponse(response_data)

        return HttpResponse('Data is saved')
    return render(request, 'question-create.html', {})

def python_view(request):

    print("okay")

    queryset = Question.objects.filter(subj = 'Python')
    return render(request, 'python.html', {'queryset':queryset})

def jquery_view(request):

    queryset = Question.objects.filter(subj = 'JQuery')
    return render(request, 'JQuery.html', {'queryset':queryset})

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