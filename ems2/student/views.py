
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory,modelformset_factory

from .forms import *
from .models import *
import json
from django.core.paginator import Paginator



@login_required(login_url='account:login')
def create_student(request):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            form = StudentForm(request.POST,request.FILES)
            if form.is_valid():
                print("valid 00000000000")
                form_data = form.save(commit=False)
                form_data.save()
                response_data = {
                    "status" : "true",
                    "title" : "Success",
                    "reLoad" : "true", 
                }
            else:
                print("not valid 00000000000")

                response_data = {
                    "status" : "false",
                    "title" : "Form validation error",
                    "reLoad" : "false",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            form = StudentForm(request.POST)
            context = {
                "form" : form,
                "page_name":"create_student",     
            }
            return render(request, 'dashboard/student/create_student.html',context)
    else:
        context = {}
        return render(request, '403.html',context)                 
            
           
                

@login_required(login_url='account:login')
def student_list(request):     
    user = request.user
    if user.is_admin:
        student = Student.objects.filter(is_deleted=False)
        paginator = Paginator(student, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj" : page_obj,
            "page_name":"Student_list",
        }
        return render(request, 'dashboard/student/list_student.html',context)
    else:
        context = {}
        return render(request, '403.html',context)
@login_required(login_url='account:login')
def view_student(request,pk): 
    user = request.user
    if user.is_admin:
        student = Student.objects.get(pk=pk)
        context = {
            "student" : student,   
            "page_name": "view_Student",
        }
        return render(request, 'dashboard/student/view_student.html',context)
    else:
        context = {}
        return render(request, '403.html', context)


@login_required(login_url='account:login')
def update_student(request,pk):     
    user = request.user
    if user.is_admin:
        if request.method == "POST":
            instance = Student.objects.get(pk=pk)
            form = StudentForm(request.POST,request.FILES,instance=instance)
            
            if (form.is_valid()):
                form.save()
                response_data = {
                "status" : "true",
                "title" : "Success",
                "reLoad" : "true",
                }
            return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        else:
            instance = Student.objects.get(pk=pk)
            form = StudentForm(instance = instance)
            context = {
                "form" : form,
                "instance" :instance,
                "page_name": "update_Student",
 
            }
            return render(request, 'dashboard/student/update_student.html',context)
    else:
        context = {}
        return render(request, '403.html',context) 


@login_required(login_url='account:login')
def delete_student(request,pk):     
    user = request.user
    if user.is_admin:
        Student.objects.get(pk=pk).delete()
        return redirect("student:list_student")
    else:
        context = {}
        return render(request, '403.html',context)

# /////////////////////////////////////////                                         
# ///////////////////////////////////////////////////////
