from django.shortcuts import render

def home(request):
    return render(request, 'vpsBase/index.html')

def contact(request):
    return render(request, 'vpsBase/contact.html')
