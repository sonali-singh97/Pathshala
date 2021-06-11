from django.urls import path
from . import views

urlpatterns = [
      path('', views.student_page, name="student"),
    path('student_profile/', views.student_page, name="student"), 
]