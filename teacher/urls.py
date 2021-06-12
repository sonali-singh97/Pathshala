from django.urls import path
from . import views

urlpatterns = [
      path('', views.teacher_page, name="teacher"),
    path('teacher_profile/', views.teacher_page, name="teacher"), 
]