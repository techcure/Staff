from django.contrib import admin
from .models import *
from django.conf import settings

# Register your models here.
# admin.site.register(User)
from django.contrib.auth.models import Group
admin.site.register(Stud)
admin.site.register(Question)
admin.site.register(ExaminPointt)


admin.site.unregister(Group)

admin.site.site_header = """ STAFF """
admin.site.site_title = "Staff Admin Portal"
admin.site.index_title = "Welcome to Staff Researcher Portal"