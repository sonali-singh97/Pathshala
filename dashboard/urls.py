from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('all-fees/', views.all_fees, name="fees"),
]