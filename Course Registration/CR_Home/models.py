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
    C_Department    = models.ForeignKey(Department, on_delete= models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['C_Code', 'C_Department'], name='unique_course'
            )
        ]