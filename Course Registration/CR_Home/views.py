from django.shortcuts import render, redirect
from .models import Course, Department
from Users.models import Student, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

S_Dictionary = {}
T_Dictionary = {}

def gen_Stu_info(usermail):
    if usermail is None:
        return
    else:
        User_QSet   = User.objects.get(email = usermail)
        U_name      = User_QSet.username
        Stu_QSet    = Student.objects.get(S_Roll = U_name)
        Dept_QSet   = Department.objects.all()

        global S_Dictionary
        S_Dictionary = {
            'Dept'        : Dept_QSet,
            'S_Details'   : Stu_QSet,
            'S_User'      : User_QSet,
        }
        return 

def gen_T_info(usermail):
    if usermail is None:
        return
    else:
        User_QSet   = User.objects.get(email = usermail)
        U_name      = User_QSet.username
        T_QSet      = Student.objects.get(S_Roll = U_name)
        Dept_QSet   = Department.objects.all()

        global S_Dictionary
        S_Dictionary = {
            'Dept'        : Dept_QSet,
            'S_Details'   : T_QSet,
            'S_User'      : User_QSet,
        }
        return 


def cr_home(request):
    
    if request.method == "POST":
        U_Email     = request.POST['Email']
        U_Password  = request.POST['Password']
        U_Status    = request.POST['ST']
        
        if U_Status == "Student":            
            gen_Stu_info(U_Email)
            Auth_User = authenticate(username = S_Dictionary['S_User'], password=U_Password)

            if Auth_User is not None:
                login(request, Auth_User)
                return render(request,'Stu_Home.html',S_Dictionary)

            else:
                return render(request,'Stu_Home.html')
                
            

        elif U_Status == "Teacher":
            gen_T_info(U_Email)
            Auth_User = authenticate(username = U_Email, password=U_Password)

            if Auth_User is not None:
                login(request,Auth_User)
                return render(request,'Stu_Home.html',T_Dictionary)

            else:
                return redirect('Stu_Home')
        
    else:
        logout(request)
        return render(request,'CR_Home.html')
    
    
    
def f_pass(request):
    return render(request,'F_pass.html')


def stu_home(request):
    return render(request,'Stu_Home.html',S_Dictionary)


def stu_course(request):            
    if request.method == "POST":
        U_Dept      = request.POST['Department']
        U_Year      = request.POST['Year']
        U_Semester  = request.POST['Semester']
        U_RegShort  = request.POST['RS'] 

        Course_QuerySet  = Course.objects.all().filter(C_Department = U_Dept,)

        Course_Dictionary ={
            'courses' : Course_QuerySet,
        }
        Course_Dictionary.update(S_Dictionary)
        return render(request,'Stu_C_Reg.html',Course_Dictionary)

    else:
        return render(request,'Stu_C_Reg.html',S_Dictionary)


def stu_edit(request):

    return render(request,'Stu_Edit.html',S_Dictionary)
