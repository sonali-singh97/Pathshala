from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, FinalResult, SubjectResult, Exam, Student_user
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.base_user import BaseUserManager

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
        if request.user == 'admin':
            logout(request)
            student_login = LoginForm()
            return render(request, 'student/login.html', {'login_form': student_login})
        return HttpResponseRedirect('/student-profile/' + str(request.user) + '/')

def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def register_students(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == "POST":
                username = request.POST['username']
                stu = Student.objects.get(pk=username)
                password = BaseUserManager().make_random_password(8, f"{username}{stu.full_name}{stu.student_class}{stu.section}")
                print(password)
                newUser = Student_user(username=username, password= password)
                newUser.save()
                signup = UserCreationForm({"username":username, "password1":password, "password2":password})
                if signup.is_valid():
                    signup.save()
                    s = Student.objects.get(pk=username)
                    s.user_created = 1
                    s.save()
                    print('successs....')
                print(username)
            students = Student.objects.all().filter(user_created=0)
            return render(request, 'student/register_student.html', {'students':students})
        else:
            return HttpResponseRedirect('/login/')    
    else:
        return HttpResponseRedirect('/admin/')

def result(request, id, exam_id):
    if request.user.is_authenticated:
        student = Student.objects.get(pk=id)
        results = FinalResult.objects.filter(student_id=id).order_by('-id')
        one_result = SubjectResult.objects.filter(student_id=id).filter(exam_id=exam_id)
        xam = Exam.objects.get(pk=exam_id)
        if student:
            return render(request, 'student/student_profile.html', {'student': student, 'results': results, 'one_result': one_result, 'exam': xam })
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')