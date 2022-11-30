from django import forms
from django.forms import ModelForm
from student.models import Student
from dal import autocomplete
from .models import Student
from django.forms.widgets import TextInput,FileInput,NumberInput,Textarea
    



 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','gender','age','email','phone','address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'age': NumberInput(attrs={'class': 'form-control','type':'nubmber',',min':'0'}),
            'gender' : forms.Select(attrs={'class': 'form-control',}),
            'email' : forms.EmailInput(attrs={'class': 'form-control',}),
            'phone' : forms.TextInput(attrs={'class': 'form-control','type':'tele','minlength':'10','maxlength':'10'}),
            'address' : forms.TextInput(attrs={'class': 'form-control',}),

        }