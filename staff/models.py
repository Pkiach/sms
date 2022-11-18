from email.policy import default
from django.db import models
from django.utils import timezone
# from course.form import departmentform
from course.models import Department,Subjects
from django.contrib.auth.models import User
from .utils import get_admin_no,get_admin_password,get_admin_username,get_password,get_lecturer_username,get_lecturer_no

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from utils import get_lecturer_no,get_password, get_admin_no,get_admin_password
# from django.contrib.auth import User

# Create your models here.
# class myusermanager(BaseUserManager):
#     def create_user(self,Firstname,Admin_number,Lastname,email,password=None):
#         if not Admin_number:
#             raise ValueError("Admin number is required")
#         if not Firstname:
#                 raise ValueError("First name is required")

#         if not Lastname:
#             raise ValueError("Last name is required")
        
#         if not email:
#             raise ValueError("email is required")

#         user=self.model(
#             Firstname=Firstname,
#             email=self.normalize_email(email),
#             Admin_number=Admin_number
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,Email,Firstname,Admin_number,Lastname,password=None):
#         user=self.create_user
#             Email=Email,
#             Firstname=Firstname,
#             Lastname=Lastname,
#             Admin_number=Admin_number,
#             password=password
#         )
#         user.is_admin=True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user


class Lecturers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Lecturernumber=models.CharField(max_length=20,unique=True)
    Title= models.CharField(max_length=16)
    Firstname=models.CharField(max_length=34)
    Middlename=models.CharField(max_length=30, blank=True)
    Lastname=models.CharField(max_length=30)
    email=models.EmailField(blank=False)
    telephonenumber=models.CharField(max_length=22)
    address=models.CharField(max_length=40)
    gender=models.CharField(max_length=15)
    IDnumber=models.CharField(max_length=15) 
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    subjects=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    is_staff=models.BooleanField(default=True)
    status=models.CharField(max_length=16,default='Inactive')
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    Timeregistered=models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return self.Lastname

   

        
       

class Admins(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Admin_number=models.CharField(max_length=20,unique=True,null=True)
    Title= models.CharField(max_length=16)
    Firstname=models.CharField(max_length=34)
    Middlename=models.CharField(max_length=30,null=True)
    Lastname=models.CharField(max_length=30)
    Email=models.EmailField(null=False,unique=True)
    Telephonenumber=models.CharField(max_length=22,unique=True)
    Address=models.CharField(max_length=40)
    Gender=models.CharField(max_length=15)
    IDnumber=models.CharField(max_length=15,unique=True)
    status=models.CharField(max_length=16,default='Inactive')
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    Timeregistered=models.DateTimeField(default=timezone.now)
    # last_login=models.BooleanField(default=False)
    # is_admin=models.BooleanField(default=True)
    # is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)
    # is_active=models.BooleanField(default=False)


#     USERNAME_FIELD='Email'
#    # PASSWORD_FIELD='Admin_number'

#     REQUIRED_FIELDS=['Admin_number','Lastname','Firstname']

#     objects=myusermanager()
#     def __str__(self):
#         return self.Firstname

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self,app_label):
#         return True 
