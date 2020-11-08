from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Permission)
admin.site.register(Instance)
admin.site.register(User, UserAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Job)