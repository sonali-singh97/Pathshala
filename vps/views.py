from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html', { 'title': "Welcome To Vimal Public School" })

def contact_page(request):
    return render(request, 'contact.html', { 'title': "Vimal Public School | Contact Us" })

def about_page(request):
    return render(request, "about.html", { "title": "Vimal Public School | About Us" })