from django.db import models
from django import forms

class About(models.Model):
    description = models.CharField(max_length=500)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    twitter = models.URLField(null=True)
    email = models.EmailField(null=True)
    contact = models.IntegerField(default=0)
    school_address = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.email

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=15)
    image = models.CharField(max_length=100)
    teacher = models.BooleanField(default=True)
    principal = models.BooleanField(default=False)