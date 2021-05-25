from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html', { 'title': "Welcome To Vimal Public School" })

def contact_page(request):
    return render(request, 'contact.html', { 'title': "Vimal Public School | Contact Us" })

def about_page(request):
    return render(request, "about.html", { "title": "Vimal Public School | About Us" })

def joinus_page(request):
    return render(request, 'about.html', { "title": "Vimal Public School | Join Us" })

def events_page(request):
    return render(request, 'events.html' , { 'title': "Vimal Public School | Events" })

def event_detail(request):
    return render(request, 'event-page.html' , { 'title': "Vimal Public School | Event Name" })

def addmission_page(request):
    return render(request, 'addmission.html')