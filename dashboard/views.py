from io import StringIO
from django.shortcuts import render
from student.models import Student_fees, Students_Class
import datetime

def dashboard(request):
     return render(request, 'dashboard/home.html')

def all_fees(request):
     allFees = Student_fees.objects.all()
     print(allFees[0])
     return render(request, 'dashboard/all_fees.html', { "allFees": allFees })

def student_promotion(request):
     print(request.POST)
     allclass = Students_Class.objects.all()
     dt = str("2021-12-12").split("-")
     exty = datetime.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
     new_session_start = exty.replace(exty.year + 1)
     new_session_end = exty.replace(exty.year + 2)
     current_session = f"{exty.year} - {exty.year + 1}"
     new_session = f"{new_session_start.year} - {new_session_end.year}"
     print(exty, new_session_start, new_session_end)
     return render(request, 'dashboard/student_promotion.html', {
          "current_session":current_session,
          "promote_session": new_session,
          "allClasses": allclass
     })

def add_expense(request):
     return render(request, 'dashboard/add_expense.html')
