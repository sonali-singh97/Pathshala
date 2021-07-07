from django.db import models

class Teacher(models.Model):
    image = models.ImageField(upload_to="images")
    teacher_id = models.IntegerField(default=0, unique=True)
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    designation = models.CharField(max_length=15)
    contact_number = models.IntegerField(default=0, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name