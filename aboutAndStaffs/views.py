from django.shortcuts import render
from aboutAndStaffs.models import About

def about(request):
    about_content = About.objects.all()
    return render(request, 'aboutAndStaffs/about.html', { 'about': about_content[0] })

def joinUs(request):
    return render(request, 'aboutAndStaffs/joinUs.html')

def staffs(request):
    return render(request, 'aboutAndStaffs/staffs.html')
