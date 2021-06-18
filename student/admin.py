from django.contrib import admin
from .models import Class_Subject, Students_Class, Student

# Register your models here.
admin.site.register(Class_Subject)
admin.site.register(Students_Class)
admin.site.register(Student)