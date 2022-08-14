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

from CR_Home.views import admin_crs, admin_crs_add, admin_home, admin_stu_edit, admin_stu_req, admin_tec, admin_tec_edit, admin_tec_req, cr_home, f_pass, admin_log, stu_home, stu_course, stu_edit, t_assign_c, t_edit, t_home, t_stu_req 
from Users.views import registration

urlpatterns = [
    #Home/Basic Pages
    path('',cr_home, name='CR_Home'),
    path('adminLog/',admin_log, name = 'Admin_Log'),
    path('regPage/',registration, name = 'CR_Reg'),
    path('f_passPage/',f_pass, name = 'F_Pass'),
    
    #Admin Pages
    path('adminHome/',admin_home, name = 'Admin_Home'),
    path('adminStuReq/',admin_stu_req, name = 'Admin_Stu_Req'),
    path('adminStuEdit/',admin_stu_edit, name = 'Admin_Stu_Edit'),
    path('adminTec/',admin_tec, name = 'Admin_Tec'),
    path('adminTecReq/',admin_tec_req, name = 'Admin_Tec_Req'),
    path('adminTecEdit/',admin_tec_edit, name = 'Admin_Tec_Edit'),
    path('adminCrs/',admin_crs, name = 'Admin_Crs'),
    path('adminCrsAdd/',admin_crs_add, name = 'Admin_Crs_Add'),

    #Student Pages
    path('stuHome/', stu_home, name = 'Stu_Home'),
    path('stuCourse/',stu_course, name = 'Stu_Course'),
    path('stuEdit/',stu_edit, name = 'Stu_Edit'),
    
    #Teacher Pages
    path('tHome/',t_home, name = 'T_Home'),
    path('tStuReq/',t_stu_req, name = 'T_Stu_Req'),
    path('tAssignC/',t_assign_c, name = 'T_Assign_C'),
    path('tEdit/',t_edit, name = 'T_Edit'),
    
    
    path('admin/', admin.site.urls),
]
