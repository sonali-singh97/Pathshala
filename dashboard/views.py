from django.shortcuts import render

def dashboard(request):
     return render(request, 'dashboard/home.html')

def all_fees(request):
     return render(request, 'dashboard/all_fees.html')
