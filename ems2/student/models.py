from __future__ import unicode_literals
from typing import Counter
from django.db import models
from datetime import datetime
from main.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from account.models import Account

class Student(BaseModel):
    name =models.CharField(max_length=20,null=True,blank=True)
    gender_status=(
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Other' , 'Other')
    )
    gender = models.CharField(choices=gender_status,max_length=6)
    age= models.IntegerField()
    email = models.EmailField(verbose_name="email", max_length=60,)
    phone =models.CharField(max_length=30,null=True,blank=True)
    address = models.TextField()
    class Meta:
        db_table = 'Students'
        verbose_name = ('Students')
        verbose_name_plural = ('Students')
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.Name)














