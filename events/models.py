from django.db import models
from django import forms

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()


class EventGallery(models.Model):
    image = models.CharField(max_length=100)
    mainImage = models.BooleanField(default=False)
    event= models.ForeignKey("Event", on_delete=models.CASCADE)

    