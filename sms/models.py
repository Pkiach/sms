
from email.policy import default
from enum import auto
from telnetlib import STATUS
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from accounts.models import User








class StudentReg(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    Regnumber=models.CharField(max_length=16,null=True)      
    Firstname=models.CharField(max_length=24,null=True)
    Middlename= models.CharField(max_length=26, null=True)
    Lastname=models.CharField(max_length=26,null=True)
    StudentEmail=models.EmailField(max_length=42,unique=True,null=True)
    IDnumber=models.CharField(max_length=9,null=True)
    ResultsSlip=models.ImageField(null=True,upload_to='image/',blank=True)
    frontID=models.ImageField(null=True, upload_to='image/',blank=True)    
    coursename=models.CharField(max_length=23,null=True)
    status=models.CharField(max_length=16,default="UNAPPROVED")     
    Telephonenumber=models.CharField(max_length=16,null=True)
    Address=models.CharField(max_length=36,null=True)
    Gender=models.CharField(max_length=12,null=True)
    DOB=models.DateTimeField(null=True)       
    photo=models.ImageField(default=False,upload_to='image/')                                  
    # backID=models.ImageField(blank=True,null=True,upload_to='image/')
    Parent_name=models.CharField(max_length=22,null=False)
    parent_email=models.EmailField(max_length=36,null=False)
    ParentTelephonenumber=models.CharField(max_length=14,null=False)            
    Timeregistered=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Firstname 
        

    

# class User(abstractUser):
#     is_admin=models.BooleanField("Is admin",default=False)
#     is_lecturer=models.BooleanField("Is lecturer",default=False)
#     is_student=models.BooleanField("Is student",default=False)


# class Lecturer_Subjects(models.Model):
#     assigning_id=models.AutoField(primary_key=True)
#     subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
#     lecturer=models.ForeignKey(Lecturers,on_delete=models.CASCADE)

