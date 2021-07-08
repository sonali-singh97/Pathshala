from django.shortcuts import render
from events.models import Event, EventGallery

def events(request):
    events_data = Event.objects.all()
    event_gallery = EventGallery.objects.all()
    # events_year = Event.objects.filter(year)
    print(events_data)
    return render(request, 'events/events.html', { 'events': events_data , 'event_images' : event_gallery })

# def events(request):
#     return render(request, 'events/events.html' )
    
def event_detail(request):
    return render(request, 'events/event-page.html')
