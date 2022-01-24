from io import StringIO
from django.shortcuts import render, HttpResponseRedirect
from student.models import Student_fees, Students_Class
import datetime

def dashboard(request):
     if request.user.is_authenticated:
          if request.user.is_staff:
               return render(request, 'dashboard/home.html')
          else:
               return HttpResponseRedirect('/login/')
     else:
          return HttpResponseRedirect('/login/')

def all_fees(request):
     if request.user.is_authenticated and request.user.is_staff:
          allFees = Student_fees.objects.all()
          print(allFees[0])
          return render(request, 'dashboard/all_fees.html', { "allFees": allFees })
     else:
          return HttpResponseRedirect('/login/')


def student_promotion(request):
     if request.user.is_authenticated and request.user.is_staff:
          print(request.POST)
          allclass = Students_Class.objects.all()
          dt = str("2021-12-12").split("-")
          exty = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
          new_session_start = exty.replace(exty.year + 1)
          new_session_end = exty.replace(exty.year + 2)
          current_session = f"{exty.year} - {exty.year + 1}"
          new_session = f"{new_session_start.year} - {new_session_end.year}"
          print(exty, current_session, new_session)
          return render(request, 'dashboard/student_promotion.html', {
               "current_session":current_session,
               "promote_session": new_session,
               "allClasses": allclass
          })
     else:
          return HttpResponseRedirect('/login/')

def add_expense(request):
     if request.user.is_authenticated and request.user.is_staff:
          return render(request, 'dashboard/add_expense.html')
     else:
          return HttpResponseRedirect('/login/')
