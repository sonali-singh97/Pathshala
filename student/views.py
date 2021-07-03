from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, FinalResult
# from .models import FinalResult
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def student_page(request, id):
    if request.user.is_authenticated:
        student = Student.objects.get(pk=id)
        results = FinalResult.objects.filter(student_id=id).order_by('-id')
        if student:
            return render(request, 'student/student_profile.html', {'student': student, 'results': results })
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def all_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            student_login = LoginForm(request, request.POST)
            if student_login.is_valid():
                student_username = student_login.cleaned_data['username']
                student_password = student_login.cleaned_data['password']
                user = authenticate(username=student_username, password=student_password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/student-profile/' + str(request.user) + '/')
        else:
            student_login = LoginForm()
        return render(request, 'student/login.html', {'login_form': student_login})
    else:
        return HttpResponseRedirect('/student-profile/' + str(request.user) + '/')

def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def register_students(request):
    return render(request, 'student/register_student.html')