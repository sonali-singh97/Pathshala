from django.shortcuts import render

def resources(request):
    return render(request, 'resources.html' )
    
def admission(request):
    return render(request, 'admission.html')
