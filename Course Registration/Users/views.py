from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from Users.models import Student, Teacher
from CR_Home.models import Department

# Create your views here.

def registration(request):
    D_Query = Department.objects.all().values 
    
    D_Dict  = {
        'Dept_Name' : D_Query,
    }

    if request.method == "POST":
        U_name    = request.POST['Name']
        U_s_t     = request.POST['ST']
        U_series  = request.POST['Series']
        U_sec     = request.POST['Section']
        U_roll    = request.POST['RollNo']
        U_reg_no  = request.POST['Reg_Id']
        U_email   = request.POST['Email']
        U_dsgn    = request.POST['Designation']
        U_dept    = request.POST['Department']
        U_pass    = request.POST['Password']
        U_cpass   = request.POST['Cpassword']

        if (U_s_t == "Student" and U_pass==U_cpass):
            dup_user = User.objects.all().filter(email = U_email)
            Flg = True
            for x in dup_user:
                if x.email == U_email:
                    Flg = False
                    break

            if Flg == True:
                myuser = User.objects.create_user(U_roll, U_email, U_pass)
                myuser.is_active = False
                myuser.save()

                Student.objects.create(
                    S_Full_Name     = U_name,
                    S_Series        = U_series,
                    S_Section       = U_sec,
                    S_Roll          = U_roll,
                    S_Reg_No        = U_reg_no,
                    S_Department    = Department(U_dept),
                )

                messages.success(request,"Account Created successfully")

                """#Verification Email
                subject = "Verify RUET Course Registration"
                message = "Hello " + U_name + " ! \n" + "Welcome to RCR! "
                from_email = settings.EMAIL_HOST_USER
                to_list = [U_email]
                send_mail(subject, message,
                            from_email, to_list,
                            fail_silently = True,)"""

                return redirect('CR_Home')

            else:
                return redirect('CR_Reg')
        
        elif (U_s_t == "Teacher" and U_pass==U_cpass):
            myuser = User.objects.create_user(U_email, U_email, U_pass)
            myuser.is_active = False
            myuser.save()

            Teacher.objects.create(
                T_Full_Name     = U_name,
                T_Email         = U_email,
                T_Designation   = U_dsgn,
                T_Department    = Department(U_dept)
            )

            return redirect('CR_Home')
        
    
    else:
        return render(request,'CR_Reg.html',D_Dict)







