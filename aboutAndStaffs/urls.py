from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('joinus/', views.joinUs, name="joinus"),
    path('staffs/', views.staffs, name="staffs")
]
