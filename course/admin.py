from django.contrib import admin


# Register your models here.
from.models import Courses,Department,Subjects,Attendance,SubjectRegistration
admin.site.register(Courses)
admin.site.register(Department)
admin.site.register(Subjects)
admin.site.register(Attendance)
admin.site.register(SubjectRegistration)
