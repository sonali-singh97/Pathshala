import datetime
from time import strptime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student, FinalResult, SubjectResult, Exam, Student_user, Student_fees
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

def payments(request, id):
    if request.user.is_authenticated:
        current_time = datetime.datetime.now()
        year = current_time.year
        month = current_time.month
        date = current_time.day
        month_name = current_time.strftime("%B")
        session_months = [f"April {year}", f"May {year}", f"June {year}", f"July {year}", f"August {year}", f"September {year}", f"October {year}", f"November {year}", f"December {year}", f"January {year}", f"February {year}", f"March {year}", f"April {year}"]
        current_month_index = session_months.index(f"{month_name} {year}")
        # current_month_index = 16
        if current_month_index <= 12:
            allFess = Student_fees.objects.filter(student_id=id)[:current_month_index + 1]
        else:
            allFess = Student_fees.objects.filter(student_id=id)[:13]
        # fee = Student_fees.objects.filter(session_year=2021).filter(session_month=4)
        # print(fee[0].id, "filtered fee")
        print(len(allFess), session_months.index(f"{month_name} {year}"), month_name,"all fees length")
        return render(request, "student/student_payments.html", { "allFees": allFess })
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
                    print(" studnet fees")
                    signup.save()

                    # Insert Fees Data for particular user
                    current_time = datetime.datetime.now()
                    year = current_time.year
                    month = current_time.month
                    date = current_time.day
                    month_name = current_time.strftime("%B")
                    student = Student.objects.get(pk=username)
                    print(student.student_class.tuition_fees, student.bus_charge, "this is student info")
                    session_months = [f"April", f"May", f"June", f"July", f"August", f"September", f"October", f"November", f"December", f"January", f"February", f"March", f"April"]
                    session_year = [year, year, year, year, year, year, year, year, year, year + 1, year + 1, year + 1, year + 1]
                    one_month_total_fees = student.bus_charge + student.student_class.tuition_fees
                    one_month_tuition_fees = student.student_class.tuition_fees
                    one_month_bus_fees = student.bus_charge
                    datetime_object = datetime.datetime.strptime("August", "%B")
                    print(datetime.datetime.strptime("August", "%B").month, "month number print")
                    for i in range(len(session_months)):
                        d = datetime.date(int(session_year[i]) ,int(datetime.datetime.strptime(session_months[i], "%B").month), 10 )
                        print(d)
                        fee = Student_fees(student_id=student, class_id=student.student_class, month_fees=one_month_tuition_fees, bus_fees=one_month_bus_fees, total_fees=one_month_total_fees, session_month_name=session_months[i], session_month=datetime.datetime.strptime(session_months[i], "%B").month, session_year=session_year[i], status="pending", is_paid=False, paid_at="-", is_message_sent=0, is_fined=False, due_date = d)

                        fee.save()





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