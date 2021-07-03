from django.db import models
from teacher.models import Teacher

class Students_Class(models.Model):
    class_name = models.CharField(max_length=10)
    strength = models.IntegerField(default=0)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    tution_fees = models.IntegerField(default=0)

    def __str__(self):
        return self.class_name

class Class_Subject(models.Model):
    name = models.CharField(max_length=10)
    class_id = models.ForeignKey(Students_Class, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    image = models.ImageField(upload_to="images", null=True)
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
    attendance = models.IntegerField(default=0)
    user_created = models.IntegerField(default=0, null=False)
    createdBy = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Exam(models.Model):
    title = models.CharField(max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubjectResult(models.Model):
    subject_id = models.ForeignKey(Class_Subject, on_delete=models.PROTECT)
    class_id = models.ForeignKey(Students_Class, on_delete=models.DO_NOTHING)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    total_marks = models.PositiveSmallIntegerField()
    obtained_marks = models.PositiveSmallIntegerField()
    isPresent = models.BooleanField(null=False)
    createdBy = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now_add=True)

class FinalResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    exam_id = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    obtained_marks = models.PositiveSmallIntegerField(default=0)
    total_marks = models.PositiveSmallIntegerField(default=0)
    percentage = models.PositiveSmallIntegerField(default=0) 