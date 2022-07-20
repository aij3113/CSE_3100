from django.contrib import admin

from .models import Reg_St_Sem, Course, Department, Reg_St_Sem, Semester, Year

# Register your models here.
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Reg_St_Sem)
admin.site.register(Course)