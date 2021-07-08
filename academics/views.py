from django.shortcuts import render
from .models import Resource

def resources(request):
    reso = Resource.objects.all()
    return render(request, 'academics/resources.html', {'resources': reso})
    
def admission(request):
    return render(request, 'academics/admission.html')
