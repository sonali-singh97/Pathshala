from django.shortcuts import render
from events.models import Event, EventGallery
from datetime import date

def events(request):
    events_data = Event.objects.all()
    event_gallery = EventGallery.objects.all()
    events_year = Event.objects.all().order_by("-date")
    print(events_year)
    todays_date = date.today()
    current_year = todays_date.year

    for event in events_data:
        event.year = int(event.getYear())

    end_year = int(events_year[len(events_year)-1].date.strftime('%Y'))
    return render(request, 'events/events.html', { 'events': events_data , 'event_images' : event_gallery, 'year_list': range(end_year, current_year+1)} )

# def events(request):
#     return render(request, 'events/events.html' )
    
def event_detail(request, id):
    event_detail = Event.objects.get(pk=id)
    event_gallery = EventGallery.objects.filter(event=id)
    main_image = EventGallery.objects.filter(event=id).filter(mainImage=True)
    print(main_image[0].image)
    for image in event_gallery:
        print("mAIN" ,image)
    return render(request, 'events/event-page.html', {"event": event_detail, "event_images": event_gallery, "main_image" : main_image[0].image})
