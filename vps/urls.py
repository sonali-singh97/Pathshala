"""vps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("vpsBase.urls")),
    path('login/', student_views.all_login, name='login'),
    path('logout/', student_views.student_logout, name='logout'),
    path('register/', student_views.register_students, name='register_students'),
    path('about/', include("aboutAndStaffs.urls")),
    path('events/', include("events.urls")),
    path('news/', include("news.urls")),
    path('academics/', include("academics.urls")),
    path('staffs/',include("aboutAndStaffs.urls")) ,
    path('student-profile/', include("student.urls")),
    path('teacher-profile/', include("teacher.urls")),
     path('dashboard/', include("dashboard.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
