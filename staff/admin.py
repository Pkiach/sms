from django.contrib import admin


#Register your models here.
from staff.models import Lecturers
from staff.models import Admins
admin.site.register(Lecturers)
admin.site.register(Admins)

