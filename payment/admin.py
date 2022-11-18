from django.contrib import admin

# Register your models here.
from. models import Payment
from. models import Semesterfees
admin.site.register(Payment)
admin.site.register(Semesterfees)