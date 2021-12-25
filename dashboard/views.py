from django.shortcuts import render
from student.models import Student_fees, Students_Class
from django.utils import timezone
import datetime

def dashboard(request):
     return render(request, 'dashboard/home.html')

def all_fees(request):
     allFees = Student_fees.objects.all()
     print(allFees[0])
     allClasses = Students_Class.objects.all()
     now = timezone.now()
     one_month_ago = datetime.datetime(now.year, now.month - 1, 1)
     data = Student_fees.objects.filter(due_date__gt=one_month_ago,
                                  due_date__lt=now)
     print(data)

     return render(request, 'dashboard/all_fees.html', { "allFees": allFees, "allClasses": allClasses })

def student_promotion(request):
     return render(request, 'dashboard/student_promotion.html')

def add_expense(request):
     return render(request, 'dashboard/add_expense.html')
