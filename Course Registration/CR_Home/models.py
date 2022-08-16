from django.db import models


# Create your models here.

#Department Table
class Department(models.Model):
    D_Name  = models.CharField(max_length=7,primary_key=True) 

#Year Table
class Year(models.Model):
    year = models.IntegerField(primary_key=True)

#Semester Table
class Semester(models.Model):
    semester = models.CharField(max_length=6, primary_key=True)

#Regular/Short Table
class Reg_St_Sem(models.Model):
    rs = models.CharField(max_length=10,primary_key= True)

#Course Table
class Course(models.Model):
    C_Code          = models.CharField(max_length=10)
    C_Title         = models.CharField(max_length=100)
    C_Credit        = models.DecimalField(decimal_places=2,max_digits=5)
    C_Department    = models.ForeignKey(Department, on_delete = models.PROTECT)
    C_Year          = models.ForeignKey(Year, on_delete = models.PROTECT, default=0)
    C_Semester      = models.ForeignKey(Semester, on_delete = models.PROTECT, default="NA")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['C_Code', 'C_Department'], name='unique_course'
            )
        ]


#Student Course Table
class Stu_Course(models.Model):
    SC_Roll        = models.IntegerField()
    SC_Year        = models.ForeignKey(Year,on_delete= models.PROTECT)
    SC_Semester    = models.ForeignKey(Semester,on_delete= models.PROTECT)
    SC_Code        = models.CharField(max_length=15)
    SC_RS_Sem      = models.ForeignKey(Reg_St_Sem, on_delete = models.PROTECT)
    SC_Dept        = models.ForeignKey(Department, on_delete= models.PROTECT)
    SC_Series      = models.IntegerField()
    SC_Section     = models.CharField(max_length=1, default= "X") 
    SC_T_AC        = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['SC_Roll', 'SC_Code', 'SC_RS_Sem', 'SC_Series'], name = 'unique_sc'
            )
        ]


#Student Course Bank Receipt
class Stu_CBR(models.Model):
    SCBR_Roll       = models.IntegerField()
    SCBR_Year       = models.ForeignKey(Year,on_delete= models.PROTECT)
    SCBR_Sem        = models.ForeignKey(Semester, on_delete= models.PROTECT)
    SCBR_RS_Sem     = models.ForeignKey(Reg_St_Sem, on_delete= models.PROTECT)
    SCBR_Dept       = models.ForeignKey(Department, on_delete= models.PROTECT)
    SCBR_Series     = models.IntegerField()
    SCBR_Section    = models.CharField(max_length=1, default="X")
    SCBR_Slip       = models.FileField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['SCBR_Roll', 'SCBR_Year', 'SCBR_Sem', 'SCBR_Series'], name = 'unique_scbr'
            )
        ]
