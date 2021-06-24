from django.db import models
from django import forms

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    pdf = models.URLField()


