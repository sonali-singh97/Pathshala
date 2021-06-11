from django.shortcuts import render

def resources(request):
    return render(request, 'academics/resources.html' )
    
def admission(request):
    return render(request, 'academics/admission.html')
