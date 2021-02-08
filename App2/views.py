from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from App.pagination import *
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

from App2.serializers import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin



class PollSerializerViewSet(viewsets.ModelViewSet):
    queryset = Polling.objects.all()
    serializer_class = PollSerializer

    pagination_class = LargeResultsSetPagination
    pagination_class = StandardResultsSetPagination
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        numbers_list = range(1, 1000)
        page = request.GET.get('page', 1)
        paginator = Paginator(numbers_list, 20)
        que_obj = PollSerializer.objects.all()

        serializer = PollSerializer(que_obj)

        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)
        return Response(serializer.data)

        queryset = Polling.objects.all()
        return Response({'data': response.data})

        context = {'queryset': queryset,}

        html = render_to_string(template_name, context)
        return HttpResponse(html)

    def list(self, request, *args, **kwargs):
        response = super(PollSerializerViewSet, self).list(request, *args, **kwargs)
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


@xframe_options_sameorigin
def displaypoll(request):

    return render(request, 'poll-index.html', {})
