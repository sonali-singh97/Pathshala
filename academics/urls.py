from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="academics"),
    path('admission/', views.resources, name="admissions"),
    path('resources/', views.admission, name="resources")
]
