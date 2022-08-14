import email
from django.shortcuts import render, redirect
from .models import Course, Department
from CR_Home.models import Semester,Year
from Users.models import Student, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

S_Dictionary = {}
T_Dictionary = {}
Admin_Dictionary = {}

def gen_admin_info(useremail):
    Admin_QSet      = Teacher.objects.get(T_Email = useremail)
    User_QSet       = User.objects.all()
    Teacher_QSet    = Teacher.objects.all().filter(T_Department = Admin_QSet.T_Department.D_Name).exclude(T_Email = useremail)
    Student_QSet    = Student.objects.all().filter(S_Department = Admin_QSet.T_Department.D_Name)
    Department_QSet = Department.objects.all()
    Semester_QSet   = Semester.objects.all()
    Year_QSet       = Year.objects.all()
    Course_QSet     = Course.objects.all().filter(C_Department = Admin_QSet.T_Department.D_Name).order_by('C_Code','C_Year','C_Semester')

    global Admin_Dictionary
    Admin_Dictionary = {
        'Admin'         : Admin_QSet,
        'Users'         : User_QSet,
        'T_Details'     : Teacher_QSet,
        'S_Details'     : Student_QSet,
        'D_Details'     : Department_QSet,
        'Sem_Details'   : Semester_QSet,
        'Y_Details'     : Year_QSet,
        'C_Details'     : Course_QSet
    }

    return


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
        T_QSet      = Teacher.objects.get(T_Email = usermail)
        Sem_QSet    = Semester.objects.all()
        Y_QSet      = Year.objects.all()
        S_QSet      = Student.objects.all().filter(S_Series = T_QSet.T_Sup_Series, S_Department = T_QSet.T_Department.D_Name, S_Section = T_QSet.T_Sup_Section)

        global T_Dictionary
        T_Dictionary = {
            'T_Details'   : T_QSet,
            'S_Details'   : S_QSet,
            'Y_Details'   : Y_QSet,
            'Sem_Details' : Sem_QSet
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
            Auth_User = authenticate(username = U_Email, password = U_Password)

            if Auth_User is not None:
                login(request,Auth_User)
                return render(request,'T_Home.html',T_Dictionary)

            else:
                return redirect('T_Home')
        
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

        Course_QuerySet  = Course.objects.all().filter(C_Department = Department(U_Dept),C_Year = Year(U_Year),C_Semester = Semester(U_Semester))
        print(Course_QuerySet)
        Course_Dictionary ={
            'RS'      : U_RegShort,
            'courses' : Course_QuerySet,
        }
        Course_Dictionary.update(S_Dictionary)
        return render(request,'Stu_C_Reg.html',Course_Dictionary)

    else:
        return render(request,'Stu_C_Reg.html',S_Dictionary)


def stu_edit(request):

    if request.method == "POST":
        Name       = request.POST['Name']
        Roll       = request.POST['Roll']
        Dept       = request.POST['Dept']
        Series     = request.POST['Series']
        Section    = request.POST['Section']
        Reg_No     = request.POST['Reg_No']
        P_Earned_C = request.POST['Prev_Earned_C'] 

        stu       = Student.objects.get(S_Roll = Roll)
        stu_user  = User.objects.get(username = Roll)

        stu.S_Full_Name     = Name
        stu.S_Department    = Department(Dept)
        stu.S_Series        = Series
        stu.S_Section       = Section
        stu.S_Reg_No        = Reg_No
        stu.S_Prev_Earned_C = P_Earned_C

        stu.save()

        gen_Stu_info(stu_user.email)

        return render(request,'Stu_Home.html',S_Dictionary)

    else:
        return render(request,'Stu_Edit.html',S_Dictionary)


def t_home(request):
    if 'delete' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        T_id   = request.POST['t_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.delete()

            user = User.objects.get(username = roll)
            user.delete()
        
        gen_T_info(T_id)
        return render(request,'T_Home.html',T_Dictionary)

    else:
        return render(request,'T_Home.html',T_Dictionary)


def t_stu_req(request):
    if 'accept' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        T_id   = request.POST['t_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.S_is_active = True
            stu.save()

            user = User.objects.get(username = roll)
            user.is_active = True
            user.save()
        
        gen_T_info(T_id)
        return render(request,'T_Home.html',T_Dictionary)

    elif 'delete' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        T_id   = request.POST['t_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.delete()

            user = User.objects.get(username = roll)
            user.delete()
        
        gen_T_info(T_id)
        return render(request,'T_Home.html',T_Dictionary)


    else:
        return render(request,'T_Stu_Req.html',T_Dictionary)



def t_assign_c(request):

    if request.method == "POST":
        Rolls       = request.POST.getlist('Rolls')
        Set_Year    = request.POST['sYear']
        Set_Sem     = request.POST['sSemester']
        Start_Date  = request.POST['S_Date']
        End_Date    = request.POST['E_Date']
 
        for roll in Rolls:
            stu       = Student.objects.get(S_Roll = roll)

            stu.S_Year      = Year(Set_Year)
            stu.S_Semester  = Semester(Set_Sem)
            stu.S_C_Start_D = Start_Date
            stu.S_C_End_D   = End_Date

            stu.save()


        return redirect('T_Assign_C')

    else:
        return render(request,'T_Assign_C.html',T_Dictionary)


def t_edit(request):

    if request.method == "POST":
        Name       = request.POST['Name']
        Dgtn       = request.POST['Designation']
        Email      = request.POST['Email']
        Dept       = request.POST['Dept'] 

        tec       = Teacher.objects.get(T_Email = Email)
        tec_user  = User.objects.get(username = Email)

        tec.T_Full_Name     = Name
        tec.T_Designation   = Dgtn
        tec.T_Department    = Department(Dept)
        tec.save()

        gen_T_info(tec_user.email)

        return render(request,'T_Home.html',T_Dictionary)

    else:
        return render(request,'T_Edit.html',T_Dictionary)


def admin_log(request):
    if request.method == "POST":
        A_Email     = request.POST['Email']
        A_Password  = request.POST['Password']

        admin_QSet = User.objects.get(username = A_Email)
        if admin_QSet.is_superuser == True:
            Auth_User = authenticate(username = A_Email, password = A_Password)
            gen_admin_info(A_Email)

            if Auth_User is not None:
                login(request,Auth_User)
                return render(request,'Admin_Home.html',Admin_Dictionary)
            
            else:
                return render(request,'Admin.html')        

        else:
            return render(request,'Admin_Home.html')

    else:
        return render(request,'Admin.html')


def admin_home(request):
    return render(request,'Admin_Home.html',Admin_Dictionary)


def admin_stu_req(request):
    if 'accept' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        Ad_id   = request.POST['admin_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.S_is_active = True
            stu.save()

            user = User.objects.get(username = roll)
            user.is_active = True
            user.save()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Home.html',Admin_Dictionary)

    elif 'delete' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        Ad_id   = request.POST['admin_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.delete()

            user = User.objects.get(username = roll)
            user.delete()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Home.html',Admin_Dictionary)



    else:
        return render(request,'Admin_Stu_Req.html',Admin_Dictionary)


def admin_stu_edit(request):
    if 'save' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        Ad_id   = request.POST['admin_id']
        
        U_year  = request.POST['Year']
        U_sem   = request.POST['Semester']
        U_sec   = request.POST['Section']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.S_Year = Year(U_year)
            stu.S_Semester = Semester(U_sem)
            stu.S_Section  = U_sec
            stu.save()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Home.html',Admin_Dictionary)

    elif 'delete' in request.POST:
        Rolls   = request.POST.getlist('Rolls')
        Ad_id   = request.POST['admin_id']

        for roll in Rolls:
            stu = Student.objects.get(S_Roll = roll)
            stu.delete()

            user = User.objects.get(username = roll)
            user.delete()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Home.html',Admin_Dictionary)
 
    else:
        return render(request, 'Admin_Stu_Edit.html',Admin_Dictionary)


def admin_tec_edit(request):
    if 'save' in request.POST:
        Emails   = request.POST.getlist('Emails')
        Ad_id   = request.POST['admin_id']
        
        for Email in Emails:
            t_dgtn  = request.POST['Designation'+Email]
            t_ser   = request.POST['T_Ser'+Email]
            t_sec   = request.POST['Sec'+Email]

            tec = Teacher.objects.get(T_Email = Email)
            tec.T_Designation   = t_dgtn
            tec.T_Sup_Series    = t_ser
            tec.T_Sup_Section    = t_sec
            tec.save()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Tec.html',Admin_Dictionary)

    elif 'delete' in request.POST:
        Emails   = request.POST.getlist('Emails')
        Ad_id   = request.POST['admin_id']

        for Email in Emails:
            tec = Teacher.objects.get(T_Email = Email) 
            tec.delete()

            user = User.objects.get(username = Email)
            user.delete()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Tec.html',Admin_Dictionary)
 
    else:
        return render(request, 'Admin_Tec_Edit.html',Admin_Dictionary)



def admin_tec(request):
    return render(request,'Admin_Tec.html',Admin_Dictionary)


def admin_tec_req(request):
    if 'accept' in request.POST:
        Emails   = request.POST.getlist('Emails')
        Ad_id   = request.POST['admin_id']

        for Email in Emails:
            tec = Teacher.objects.get(T_Email = Email)
            tec.T_is_active = True
            tec.save()

            user = User.objects.get(username = Email)
            user.is_active = True
            user.save()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Tec.html',Admin_Dictionary)

    elif 'delete' in request.POST:
        Emails   = request.POST.getlist('Emails')
        Ad_id   = request.POST['admin_id']

        for Email in Emails:
            tec = Teacher.objects.get(T_Email = Email)
            tec.delete()

            user = User.objects.get(username = Email)
            user.delete()
        
        gen_admin_info(Ad_id)
        return render(request,'Admin_Tec.html',Admin_Dictionary)

    else:
        return render(request,'Admin_Tec_Req.html',Admin_Dictionary)


def admin_crs(request):
    return render(request, 'Admin_Crs.html',Admin_Dictionary)


def admin_crs_add(request):
    if request.method == "POST":
        Ad_id       = request.POST['admin_id']

        c_code      = request.POST['C_Code']
        c_title     = request.POST['C_Title']
        c_credit    = request.POST['C_Credit']
        c_dept      = request.POST['admin_dept']
        c_year      = request.POST['Year']
        c_sem       = request.POST['Semester']

        Course.objects.create(
            C_Code       = c_code,
            C_Title      = c_title,
            C_Credit     = c_credit,
            C_Department = Department(c_dept),
            C_Year       = Year(c_year),
            C_Semester   = c_sem
        )

        gen_admin_info(Ad_id)
        return render(request, 'Admin_Crs.html',Admin_Dictionary)
        
    
    else:
        return render(request, 'Admin_Crs_Add.html',Admin_Dictionary)