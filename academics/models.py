from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    createdOn = models.DateField()
    pdf = models.URLField()
