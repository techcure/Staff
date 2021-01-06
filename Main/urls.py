
from django.contrib import admin

from django.conf import settings

from django.urls import include, path
from rest_framework import routers
from App import views
from App.views import *
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Question', views.QuestionViewSet)
router.register(r'Question', views.QuestionViewSet)
router.register(r'Student', views.StudViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ques-view/', QuestionList.as_view()),
    path('ques-detail/<int:pk>/', QuestionDetail.as_view()),
	path('question-create/', index_create, name='question-create'),
	path('index_view/', index_view, name='index_view'),
	path('python_view/', python_view, name='python_view'),
	path('jquery_view/', jquery_view, name='jquery_view'),
]