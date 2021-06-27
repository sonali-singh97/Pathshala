from django.db import models
from django import forms
import datetime

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date =models.DateField()
    pdf = forms.FileField()

    def __str__(self):
        return self.title


