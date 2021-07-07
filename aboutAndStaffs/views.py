from django.shortcuts import render
from aboutAndStaffs.models import About
from teacher.models import Teacher

def about(request):
    about_content = About.objects.all()
    principal = Teacher.objects.get(designation="principal")
    return render(request, 'aboutAndStaffs/about.html', { 'about': about_content[0], 'principal': principal })

def joinUs(request):
    return render(request, 'aboutAndStaffs/joinUs.html')

def staffs(request):
    teacher = Teacher.objects.all()
    return render(request, 'aboutAndStaffs/staffs.html', {'teachers': teacher})
