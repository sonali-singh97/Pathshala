from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name="events"),
    path('event-detail/', views.event_detail, name="event-detail")
]