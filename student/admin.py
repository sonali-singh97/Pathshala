from django.contrib import admin
from .models import Class_Subject, Students_Class, Student, Fee_Type, Fee_Transaction, Payment

# Register your models here.
admin.site.register(Class_Subject)
admin.site.register(Students_Class)
admin.site.register(Student)
admin.site.register(Fee_Type)
admin.site.register(Fee_Transaction)
admin.site.register(Payment)

