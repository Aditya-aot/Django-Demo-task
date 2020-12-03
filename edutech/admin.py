from django.contrib import admin
from .models import Question_Asked ,Answer_model
from django.contrib.auth.models import  User, auth
from django.contrib.auth.admin import UserAdmin


admin.site.register(Question_Asked)

admin.site.register(Answer_model)
