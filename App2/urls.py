

from django.urls import include, path
from rest_framework import routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from django.conf import settings

app_name = 'App2'

urlpatterns = [

    path('poll-index/', PollSerializerViewSet.as_view({'get': 'list'}), name='poll-index'),
    path('polling-index/', displaypoll, name='polling-index')


]

format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)