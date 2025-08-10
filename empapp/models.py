from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class leave(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default="")
    type=models.CharField(max_length=100)
    reason=models.CharField(max_length=500)
    date=models.DateField()
    hours=models.IntegerField()
    status=models.ImageField(default=0)
    created=models.DateTimeField(auto_now_add=True)

    class meta:
        db_table='leave'