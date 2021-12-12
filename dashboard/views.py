from django.shortcuts import render
from student.models import Student_fees

def dashboard(request):
     return render(request, 'dashboard/home.html')

def all_fees(request):
     allFees = Student_fees.objects.all()
     print(allFees[0])
     return render(request, 'dashboard/all_fees.html', { "allFees": allFees })
<<<<<<< HEAD

def student_promotion(request):
     return render(request, 'dashboard/student_promotion.html')

def add_expense(request):
     return render(request, 'dashboard/add_expense.html')
=======
>>>>>>> 857da949e7a5e7659c4e738d18137368bda6639a
