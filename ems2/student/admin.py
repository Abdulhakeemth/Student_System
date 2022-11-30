from django.contrib import admin
from student.models import *
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','gender','age','email','phone','address']
admin.site.register(Student,StudentAdmin)


