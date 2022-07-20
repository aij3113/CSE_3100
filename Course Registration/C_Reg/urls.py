"""C_Reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include,path

from CR_Home.views import cr_home, f_pass, stu_home, stu_course, stu_edit
from Users.views import registration

urlpatterns = [
    path('',cr_home, name='CR_Home'),
    path('regPage/',registration, name='CR_Reg'),
    path('f_passPage/',f_pass, name='F_Pass'),
    path('stuHome/', stu_home, name='Stu_Home'),
    path('stuCourse/',stu_course, name='Stu_Course'),
    path('stuEdit',stu_edit, name = 'Stu_Edit'),
    path('admin/', admin.site.urls),
]
