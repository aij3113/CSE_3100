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
from django.conf.urls.static import static
from django.conf import settings

from CR_Home.views import admin_crs, admin_crs_add, admin_crs_edit, admin_home, admin_stu_edit
from CR_Home.views import stu_course_com, t_assign_c_com, t_assign_c_req, admin_stu_req, admin_change
from CR_Home.views import admin_stu, admin_tec_edit, admin_tec_req, cr_home, f_pass, admin_log
from CR_Home.views import stu_home, stu_course, stu_edit, t_assign_c, t_edit, t_home, t_stu_req
from CR_Home.views import pass_change 
from Users.views import registration

urlpatterns = [
    #Home/Basic Pages
    path('',cr_home, name='CR_Home'),
    path('adminLog/',admin_log, name = 'Admin_Log'),
    path('regPage/',registration, name = 'CR_Reg'),
    path('fPass/',f_pass, name = 'F_Pass'),
    path('<uidb64>/<token>', pass_change, name='PChange'),
    
    #Admin Pages
    path('adminHome/',admin_home, name = 'Admin_Home'),
    path('adminTecReq/',admin_tec_req, name = 'Admin_Tec_Req'),
    path('adminTecEdit/',admin_tec_edit, name = 'Admin_Tec_Edit'),
    path('adminChange/', admin_change, name = 'Admin_Change'),
    path('adminStu/',admin_stu, name = 'Admin_Stu'),
    path('adminStuReq/',admin_stu_req, name = 'Admin_Stu_Req'),
    path('adminStuEdit/',admin_stu_edit, name = 'Admin_Stu_Edit'),
    path('adminCrs/',admin_crs, name = 'Admin_Crs'),
    path('adminCrsAdd/',admin_crs_add, name = 'Admin_Crs_Add'),
    path('adminCrsEdit/',admin_crs_edit, name = 'Admin_Crs_Edit'),

    #Student Pages
    path('stuHome/', stu_home, name = 'Stu_Home'),
    path('stuCourse/',stu_course, name = 'Stu_Course'),
    path('stuCourseCom/',stu_course_com, name = 'Stu_Course_Com'),
    path('stuEdit/',stu_edit, name = 'Stu_Edit'),
    
    #Teacher Pages
    path('tHome/',t_home, name = 'T_Home'),
    path('tStuReq/',t_stu_req, name = 'T_Stu_Req'),
    path('tAssignC/',t_assign_c, name = 'T_Assign_C'),
    path('tAssignCReq/',t_assign_c_req, name = 'T_Assign_C_Req'),
    path('tAssignCCom/',t_assign_c_com, name = 'T_Assign_C_Com'),
    path('tEdit/',t_edit, name = 'T_Edit'),

    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

