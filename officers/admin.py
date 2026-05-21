from django.contrib import admin
from .models import Officer, LoginLog
admin.site.register(Officer)
admin.site.register(LoginLog)