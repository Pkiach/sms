import email
from multiprocessing import context
from random import random,choice
from telnetlib import LOGOUT
from turtle import title
from django.shortcuts import redirect, render

# from accounts.views import signUp
from.models import Lecturers,Admins
from django.contrib import messages
from .form import Lecturersform,adminform,Loginstaffform
from django.contrib.auth.models import User
from course. models import Department,Subjects
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# @login_required (login_url='loginstaff')
def staffhome(request):
    lecturer=Lecturers.objects.filter(email=request.user.email).first()
    return render(request,'staff/staffhome.html',{"lecturer":lecturer})

# @login_required (login_url='login')
def staffinformation(request):
    title="Lecturers List"
    queryset=Lecturers.objects.all()
    context={
        "title":title,
        "queryset":queryset,

    }
    return render(request,'staff/staffinfo.html',context)


# @login_required (login_url='login') 
def delete_staff(request,id):
    number=Lecturers.objects.get(id=id)
    if request.method=="POST":
        number.delete()       
        return redirect("{% url 'staffinfo' %}") 
    else:
        context={      
        "item":number,
         }
    return render(request,'course/detele.html',context)

# @login_required (login_url='login')
def lectuer_class_attendance(request):
    return render(request,'lec_class_attendance.html')

# @login_required (login_url='login')
def get_lecturer_no(code):
        lecturer_no=f"{code}"# AC regnumber=AC
        two_no=(ord(code[0])+ord(code[1]))%26
        r_no="".join([str(choice([1,2,3,4,5,6,7,8,9,0])) for _ in range(5)])
        lecturer_no=f"{lecturer_no}{two_no}{r_no}"# regnumber= AC17/0756
        return lecturer_no

# @login_required (login_url='login')
def get_lecturer_username(Firstname):
    return f"{Firstname}"

# @login_required (login_url='login')
def get_password(Firstname):
    return make_password (f"{Firstname}1234")# password geofrey1234


# @login_required (login_url='login')
def get_lecturer_email(email,msg):
    send_mail(
        subject="Elgon View College",
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email)


# @login_required (login_url='login')
def registstaff(request):
    title='staff Registration'
    form=Lecturersform(request.POST or None)

    if form.is_valid():
        
        title= form.cleaned_data['Title']
        f_name=form.cleaned_data['Firstname']
        m_name=form.cleaned_data['Middlename']   
        l_name=form.cleaned_data['Lastname']
        email=form.cleaned_data['email']
        t_number=form.cleaned_data['telephonenumber']
        address=form.cleaned_data['address']
        gender=form.cleaned_data['Gender']
        id=form.cleaned_data['IDnumber']
        code=form.cleaned_data['department']
        subject=form.cleaned_data['subjects']
        # status=form.cleaned_data['status']     
        mail=Lecturers.objects.filter(email=email)         
 
        if len(mail)>0: 
            messages.info(request,'Lecturer already exist')
            return redirect("loginstaff")
        else:
            department=Department.objects.filter(dept_code=code).first()
            sub=Subjects.objects.filter(subjectcode=subject).first()
            p=Lecturers(Title=title,Firstname=f_name,Middlename=m_name,Lastname=l_name,email=email,
            telephonenumber=t_number,address=address,gender=gender,IDnumber=id,department=department,
            subjects=sub)
                        
            # p=Lecturers           
            # dept=lecturer.dept_code
            user=User(email=p.email)
            
           # course_code=Courses.objects.filter(coursename=name).first()
            Lecturernumber=get_lecturer_no(code)
            p.Lecturernumber=Lecturernumber
            p.save()                
            user.username=get_lecturer_username(p.Firstname)
            user.password=get_password(p.Firstname)    
            user.save() 
            msg= f"""
         
        
        Your Lecturer_no: {Lecturernumber},
        and your login credentials are:

    
        username: {p.Firstname}, 
        password: {p.Firstname}1234 
        """
        # get_lecturer_email(p.email,msg)
        # messages.success(request,f"{user.username} {user.password}") 

        return redirect("loginstaff")
    else:
        context={
            'title':title,
            'form':form
            }
        return render(request,'staff/regist.html',context)


def login_staff(request):
    form=Loginstaffform()
    if request.method=="POST":
        form=Loginstaffform(request.POST)
        if form.is_valid():  
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.get(username=username) 
            if check_password(password,user.password):                 
                login(request,user)               
                # redirect to the next page
                return  redirect("adminpage")
            else:
                #either username or passaword is incorrect
                messages.error(request,'Invalid username or password')           
                form=Loginstaffform()
                return render(request,'staff/signin_staff.html',{"form":form})                
        else:
            messages.error(request,f'Form is not valid {form.cleaned_data}')     
    context={        
        "form": form
        }
    return render(request,'staff/signin_staff.html',context) 

@login_required (login_url='login')
def logoutstaff(request):
    logout(request)
    return redirect("home")


# @login_required (login_url='login')
def get_admin_username(Firstname):
    return f"{Firstname}"



# @login_required (login_url='login')    
def get_admin_no():
        # admin_no=f"{dept_code}"# AC regnumber=AC
        # two_n0=(ord(dept_code[0])+ord(dept_code[1]))%26
        admin_no="".join([str(choice([1,2,3,4,5,6,7,8,9,0])) for _ in range(6)])
        # lecturer_no=f"{lecturer_no}{r_no}"# regnumber= AC17/0756/
        return admin_no

# @login_required (login_url='login')
def get_admin_password(Firstname):
    return  make_password(f"{Firstname}1234")# password geofrey1234


# @login_required (login_url='login')
def staffadmin(request):
    title='ADD Admin'
    form=adminform(request.POST or None)  
    if form.is_valid(): 
        Title= form.cleaned_data['Title']
        Firstname=form.cleaned_data['Firstname']
        Middlename=form.cleaned_data['Middlename']   
        Lastname=form.cleaned_data['Lastname']
        Email=form.cleaned_data['Email']
        Telephonenumber=form.cleaned_data['Telephonenumber']
        Address=form.cleaned_data['Address']
        Gender=form.cleaned_data['Gender']
        IDnumber=form.cleaned_data['IDnumber']
       

        p=Admins(Title=Title, Firstname=Firstname,Middlename=Middlename,Email=Email,Telephonenumber=Telephonenumber,Address=Address,Gender=Gender,IDnumber=IDnumber)           
              
        user=User(email=p.Email)        
        Admin_number=get_admin_no()
        p.Admin_number=Admin_number
        p.save()                
        user.username=get_admin_username(p.Firstname)
        user.password=get_password(p.Firstname)    
        user.save() 
        msg= f"""
         
        
        Your Lecturer_no: {Admin_number},
        and your login credentials are:

    
        username: {p.Firstname}, 
        password: {p.Firstname}1234 
        """       

        return redirect('loginstaff')
    context={
            'title':title,
            "form":form
    }
    return render(request,'staff/registeradmin.html',context)


# def login_admin(request):
#     #form=adminform()
#     if request.method=="POST": 
#         username=request.POST.get('Firstname')
#         password=request.POST.get('Admin_number')
        
#         user = authenticate(request, Firstname=username, Admin_number=password)
#         if admins is not None:
#             login(request, user)
#             # redirect to the next page
#             return redirect('staffadmin')
#         else:
#             #either username or passaword is incorrect
#             messages.info(request,'The username/password is incorrect  ')
            
#     else: 
#     #  context={
#     #     'form':form
#     # }      
    
#         return render(request,'staff/login_admin.html') 






