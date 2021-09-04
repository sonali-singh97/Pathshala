from django.contrib import admin
from .models import Class_Subject, Students_Class, Student, SubjectResult, Exam, Student_user, FinalResult, Student_fees

class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_id')

admin.site.register(Class_Subject, ClassSubjectAdmin)

class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'class_teacher', 'tuition_fees')

admin.site.register(Students_Class, StudentClassAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'student_class', 'section', 'father_contact')

admin.site.register(Student, StudentAdmin)

class SubjectResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'class_id', 'subject_id', 'obtained_marks')

admin.site.register(SubjectResult, SubjectResultAdmin)

class FinalResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'exam_id', 'percentage')

admin.site.register(FinalResult, FinalResultAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class StudentUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

class StudentFeesAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'class_id', 'is_paid')

admin.site.register(Student_fees, StudentFeesAdmin)

admin.site.register(Exam, ExamAdmin)
admin.site.register(Student_user, StudentUserAdmin)


