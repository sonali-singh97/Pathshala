from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.resources, name="admission"),
    path('resources/', views.admission, name="resources")
]
