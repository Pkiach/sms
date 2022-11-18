from email.policy import default
from django.db import models



from sms.models import StudentReg
from payment.models import Semesterfees,Payment


class Courses(models.Model):
    course_code=models.CharField(max_length=19 ,blank=False,primary_key=True)
    course_name=models.CharField(max_length=120)



class Department(models.Model):
    school_id=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    dept_code=models.CharField(max_length=20, primary_key=True)
    department_name=models.CharField(max_length=100)
   

class Subjects(models.Model):
    subjectcode=models.CharField(max_length=10,primary_key=True)
    subject_name=models.CharField(max_length=100)
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    

class SubjectRegistration(models.Model):
    registration_id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(StudentReg,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)    
    term_id=models.ForeignKey(Semesterfees,on_delete=models.CASCADE )
    


class Attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    unit=models.ForeignKey(SubjectRegistration,on_delete=models.CASCADE,null=True)
    present=models.IntegerField(default=0) 
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()










