import datetime

from django.db import models
from rft_webapp.math.enums import Type

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=28)


class Results(models.Model):
    type = models.IntegerField()
    time = models.DurationField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)