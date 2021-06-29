from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .models import FinalResult

def student_page(request, id):
    student = Student.objects.get(pk=id)
    results = FinalResult.objects.filter(student_id=id).order_by('-id')
    if student:
        return render(request, 'student/student_profile.html', {'student': student, 'results': results })
    else:
        return HttpResponseRedirect('/')