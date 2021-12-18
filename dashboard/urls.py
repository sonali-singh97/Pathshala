from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('all-fees/', views.all_fees, name="all-fees"),
    path('student-promotion/', views.student_promotion, name="promotion"),
    path('add-expense/', views.add_expense, name="add-expense")
]