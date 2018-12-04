from django.db import models


# Create your models here.

class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField()
    time = models.FloatField()
