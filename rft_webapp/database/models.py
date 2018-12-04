from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Results(models.Model):
    user = models.IntegerField()
    type = models.IntegerField(default=None)
    score = models.IntegerField(default=None)
    time = models.FloatField(default=None) 
