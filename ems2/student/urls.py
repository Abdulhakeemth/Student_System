
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    
    path('student-create/', views.create_student, name="create_student"),
    path('student-list/',views.student_list, name="list_student"),
    path('student-view/<pk>/', views.view_student, name="view_student"),
    path('student-update/<pk>/', views.update_student, name="update_student"),
    path('student-delete/<pk>/',views.delete_student, name="delete_student"),


    

]

