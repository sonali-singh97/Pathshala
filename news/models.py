from django.db import models
from django import forms
import datetime

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date =models.DateField()
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.title
    
    def datepublished(self):
        return self.date.strftime('%d')

    def monthpublished(self):
        return self.date.strftime('%b')

    def yearpublished(self):
        return self.date.strftime('%Y')



