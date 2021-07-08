from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.student_page, name="student"),
    path('<int:id>/<int:exam_id>', views.result ,name="student_with_result")
]