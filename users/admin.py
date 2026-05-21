# from django.contrib import admin

# from .models import Citizen

# admin.site.register(Citizen)
# # Register your models here.

# from django.contrib import admin
# from django.contrib.auth.models import Group
# from .models import Citizen

# admin.site.register(Citizen)
# # Register your models here.
# admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from .models import Citizen

try:
    admin.site.unregister(Group)
except NotRegistered:
    pass

try:
    admin.site.unregister(User)
except NotRegistered:
    pass

class CustomUserAdmin(UserAdmin):
    list_filter = []
    list_display = ['username', 'email']
    search_fields = []
    actions = None
    def has_add_permission(self, request):
        return False
admin.site.register(User, CustomUserAdmin)
admin.site.register(Citizen)