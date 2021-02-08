

from django.urls import include, path
from rest_framework import routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from django.conf import settings

app_name = 'App'

urlpatterns = [
    path('ques-detail/<int:pk>/', QuestionDetail.as_view()),
    path('index-viewset/', IndexViewSet.as_view({'get': 'list'}), name='index-viewset'),
    path('python_view/', PythonViewSet.as_view({'get': 'list'}), name = 'python_view'),
    path('jquery_view/', JQueryViewSet.as_view({'get': 'list'}), name='jquery_view'),
    path('stud_view/', StudentViewSet.as_view({'get': 'list'}), name='stud_view'),
    path('html_view/', HTMLViewSet.as_view({'get': 'list'}), name = 'html_view'),
    path('stu_detail/', StudentViewSet.as_view({'get': 'list'}), name='stu_detail'),
    path('examinpoint/', ExaminPointViewSet.as_view({'get': 'list'}),name = 'examinpoint'),


    path('display-python-que/', display_python_que.as_view()),
    path('<pk>/update_question', UpdateQuestion.as_view()),

    path('display-python/', DisplayPython.as_view(), name='display-python'),


    path('create-user/', DisplayUser.as_view(), name='create-user'),

    
    path('display-jquery/', DisplayJquery.as_view(), name='display-jquery'),
    path('display-html/', DisplayHTML.as_view(), name='display-html'),
    path('question_op/<int:pk>/', question_op, name='question_op'),
    path('question_put/<int:pk>/', question_put, name='question_put'),
    path('take-test/', DisplayStudents.as_view(), name='take-test'),
    path('test-results/', DisplayResult.as_view(), name='test-results'),
    
]

format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
