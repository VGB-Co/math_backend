from django.db import models


# Create your models here.

class Results(models.Model):
    user = models.CharField(max_length=30)
    type = models.IntegerField()
    time = models.FloatField()
