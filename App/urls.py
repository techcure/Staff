

from django.urls import include, path
from rest_framework import routers
from .views import *

from django.conf.urls import url
app_name = 'App'

urlpatterns = [
    path('ques-detail/<int:pk>/', QuestionDetail.as_view()),
    path('question-create/', IndexViewSet.as_view({'get': 'list'}), name='question-create'),
    path('python_view/', PythonViewSet.as_view({'get': 'list'}), name = 'python_view'),
    path('jquery_view/', JQueryViewSet.as_view({'get': 'list'}), name='jquery_view'),
    path('stud_view/', StudentViewSet.as_view({'get': 'list'}), name='stud_view'),
    path('html_view/', HTMLViewSet.as_view({'get': 'list'}), name = 'html_view'),

    path('display-python-que/', display_python_que.as_view()),
    path('<pk>/update_question', UpdateQuestion.as_view()),

    path('display-python/', DisplayPython.as_view(), name='display-python'),
    path('display-jquery/', DisplayJquery.as_view(), name='display-jquery'),
    path('display-html/', DisplayHTML.as_view(), name='display-html'),
]