from django.shortcuts import render

def about(request):
    return render(request, 'aboutAndStaffs/about.html')

def joinUs(request):
    return render(request, 'aboutAndStaffs/joinUs.html')

def staffs(request):
    return render(request, 'aboutAndStaffs/staffs.html')
