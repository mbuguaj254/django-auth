from django.contrib import admin
from .models import Goal, User_profile
# Register your models here.
admin.site.register(User_profile)

admin.site.register(Goal)