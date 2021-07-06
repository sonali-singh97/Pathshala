from django.db import models

class About(models.Model):
    logo = models.ImageField(upload_to="images")
    description = models.TextField(max_length=500)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    twitter = models.URLField(null=True)
    email = models.EmailField(null=True)
    contact = models.IntegerField(default=0)
    school_address = models.CharField(max_length=20, null=True)
    about_video = models.FileField(upload_to="video")

    def __str__(self):
        return self.email