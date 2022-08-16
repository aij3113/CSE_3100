from django.contrib import admin

from Users.models import Student, Teacher

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)

