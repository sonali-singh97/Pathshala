from django.shortcuts import render

def events(request):
    return render(request, 'events.html' )
    
def event_detail(request):
    return render(request, 'event-page.html')
