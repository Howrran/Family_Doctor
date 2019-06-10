from django.db import models

# Create your models here.

class Schedule(models.Model):
    clinic = models.CharField(max_length=150, default='')
    doctor = models.CharField(max_length=150, default='')
    time = models.IntegerField()
    day = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

class History(models.Model):
    username = models.CharField(max_length=150)
    desease = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)