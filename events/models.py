from django.db import models
from django import forms

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name
    
    def day(self):
        return self.date.strftime('%d')

    def month(self):
        return self.date.strftime('%b')

    def year(self):
        return self.date.strftime('%Y')


class EventGallery(models.Model):
    image = models.ImageField(upload_to="images")
    mainImage = models.BooleanField(default=False)
    event= models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name

    