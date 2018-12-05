from django.db import models

# Create your models here.

class Results(models.Model):
    name = models.TextField()
    type = models.IntegerField(default=None)
    score = models.IntegerField(default=None)
    time = models.FloatField(default=None)
