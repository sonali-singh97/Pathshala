from django.shortcuts import render

def student_page(request):
    return render(request, 'student/student_profile.html' )