from django.db import models

# Create your models here.
class Students_Class(models.Model):
    class_name = models.CharField(max_length=10)
    strength = models.IntegerField(default=0)
    class_teacher = models.CharField(max_length=15)
    tution_fees = models.IntegerField(default=0)

class Class_Subject(models.Model):
    name = models.CharField(max_length=10)
    class_id = models.ForeignKey(Students_Class, on_delete=models.PROTECT)

class Student(models.Model):
    student_id = models.IntegerField(default=0)
    full_name = models.CharField(max_length=20)
    student_class = models.ForeignKey(Students_Class, on_delete=models.PROTECT)
    section = models.CharField(max_length=1)
    session_start = models.DateField()
    session_end = models.DateField()
    dob = models.DateField()
    father_name = models.CharField(max_length=20)
    contact_number = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    attendence = models.IntegerField(default=0)
    createdBy = models.CharField(max_length=20)
    createdAt = models.DateTimeField()