from django.db import models
from sms.models import StudentReg
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    student_number=models.ForeignKey(StudentReg,on_delete=models.CASCADE)
    telephone_number=models.IntegerField()    
    amount_paid=models.IntegerField() 
    # status=models.CharField(max_length=16,default="INCOMPLETE")   
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Payment made by"+str(self.student_number)



class Semesterfees(models.Model):    
    semester=models.IntegerField(primary_key=True)
    fees=models.IntegerField()
    year=models.CharField(max_length=7)
    status=models.CharField(max_length=20,default="Inactive")


class Feesdata(models.Model):
   
    student_id=models.ForeignKey(StudentReg,on_delete=models.CASCADE)
    semester_id=models.ForeignKey(Semesterfees,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=12,default="INCOMPLETE")
    class Meta:
        unique_together=["student_id","semester_id"]