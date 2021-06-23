from django.shortcuts import render

def teacher_page(request):
    return render(request, 'teacher/teacher_profile.html' )