
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
router.register(r'Student', views.StudViewSet)

app_name = 'App'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    # path('accounts/signup/staff/', StaffSignUpView.as_view(), name='staff_signup'),

    path('admin/', admin.site.urls),
    path('home1/', Home1, name='home1'),
    path('', include(router.urls)),
    url(r'^',include('App.urls',namespace='App')),
    url(r'^',include('App2.urls')),
    path('ques-view/', QuestionList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
