from datetime import date
from django.db import models

from CR_Home.models import Department, Semester, Year

# Create your models here.

#Student Table
class Student (models.Model):
    S_Roll          = models.IntegerField(primary_key = True)
    S_Full_Name     = models.CharField(max_length = 100)
    S_Series        = models.IntegerField()
    S_Section       = models.CharField(max_length = 1)
    S_Reg_No        = models.IntegerField()
    S_Prev_Earned_C = models.DecimalField(decimal_places = 2, max_digits = 5, default = 0.0)
    S_Department    = models.ForeignKey(Department, on_delete = models.PROTECT)
    S_Year          = models.ForeignKey(Year, on_delete = models.PROTECT ,default = 0)
    S_Semester      = models.ForeignKey(Semester, on_delete = models.PROTECT, default = "NA") 
    S_C_Start_D     = models.DateField(default = ('2099-01-01'))
    S_C_End_D       = models.DateField(default = date.today)
    S_is_active     = models.BooleanField(default = False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['S_Roll', 'S_Reg_No',], name='unique_Roll_Reg'
            )
        ]
        

#Teacher Table
class Teacher (models.Model):
    T_Full_Name     = models.CharField(max_length = 100)
    T_Email         = models.EmailField(primary_key = True)
    T_Department    = models.ForeignKey(Department,on_delete= models.PROTECT)
    T_Designation   = models.CharField(max_length=30, default = "Not Added")
    T_Sup_Series    = models.IntegerField(default = 0)
    T_Sup_Section   = models.CharField(max_length = 1, default = "x")
    T_is_active     = models.BooleanField(default = False)

