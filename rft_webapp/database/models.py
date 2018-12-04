from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Results(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.IntegerField()
    time = models.FloatField() 
