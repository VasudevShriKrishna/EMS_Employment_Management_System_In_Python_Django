from email.policy import default
from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
class Emp(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/',default='default.jpg')
    skill =models.CharField(max_length=500 ,default=" ")

    
    def __str__(self):
        return self.name


class attendance(models.Model):
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    clock=models.IntegerField(default=0)
    timein=models.TimeField(default='00:00',blank=True,null=True)
    timeout=models.TimeField(default='00:00')
    date=models.DateField(auto_now_add=True)


    def totalhours(self):
        a = self.timein
        b = self.timeout
        enter_delta = datetime.timedelta(hours=a.hour, minutes=a.minute, seconds=a.second)
        exit_delta = datetime.timedelta(hours=b.hour, minutes=b.minute, seconds=b.second)
        delta = exit_delta - enter_delta
        return delta

