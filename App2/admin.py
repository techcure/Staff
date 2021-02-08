from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import *
from django.conf import settings

admin.site.register(Polling)


