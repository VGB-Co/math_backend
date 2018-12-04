from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Results(models.Model):
    user = models.IntegerField()
    type = models.IntegerField()
    score = models.IntegerField()
    time = models.FloatField()

    class Meta:
        managed = True
