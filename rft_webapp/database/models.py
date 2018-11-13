from django.db import models


# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, null=False, unique=True)


class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField()
    time = models.FloatField()
