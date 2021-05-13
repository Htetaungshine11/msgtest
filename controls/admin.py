from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuser
# Register your models here.
admin.site.register(Cuser,UserAdmin)