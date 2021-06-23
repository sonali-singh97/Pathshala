from django.db import models

class Teacher(models.Model):
    teacher_id = models.IntegerField(default=0, unique=True)
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    designation = models.CharField(max_length=15)
    contact_number = models.IntegerField(default=0, unique=True, max_length=10)
    createdAt = models.DateTimeField()

    def __str__(self):
        return self.full_name