from ast import Str
from datetime import date
from email import message
import email
from email.errors import MessageError
from enum import auto
from msilib.schema import Font
from multiprocessing import context
from random import random,choice
from re import S, template
from tkinter import Canvas
from unicodedata import name
from unittest import loader
from webbrowser import get
from xmlrpc.client import DateTime
from django.shortcuts import redirect, render
from django.http import HttpResponse

from myfinal.settings import EMAIL_HOST_USER
#from sms.form import studForm
from .form import studForm,RegisterForm,searchform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StudentReg 
from course.models import Courses
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
from xhtml2pdf import pisa




# Generate students report
 
def students_information(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0 )
    #Create a text object
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    #add lines of text

    

    queryset=StudentReg.objects.all()
    lines=[]

    for stdreg in queryset:
        lines.append("=====================Pkiach Report=============================")
        lines.append(f"Registration Number: {stdreg.Regnumber}")
        lines.append(f"First Name: {stdreg.Firstname}")
        lines.append(f"Middle Name: {stdreg.Middlename}")
        lines.append(stdreg.Lastname)
        lines.append(f"Email: {stdreg.StudentEmail}")
        lines.append(stdreg.Telephonenumber)
        # lines.append(StudentReg.Address)
        lines.append(stdreg.Gender)
        # lines.append(StudentReg.DOB)
        lines.append(f"Id Number: {stdreg.IDnumber}")
        lines.append(f"Course: {stdreg.coursename}")
        # lines.append(StudentReg.Birthcertificatenumber)
        lines.append(stdreg.Parent_name)
        # lines.append(StudentReg.Email)
        lines.append(stdreg.ParentTelephonenumber)
        lines.append("===========================End of report=================================")
        lines.append(" ")

    #loop
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename="students_information.pdf")  







def home(request):
    return render(request,"home.html")

def about_us(request):
    return render(request,'about us.html',{'name':'about'})


#@login_required (login_url='login')
def staff(request):
    return redirect("loginstaff")


def contacts(request):
    return render(request,'contacts.html',{'name':'contacts'})


# @login_required (login_url='login')
def students(request):
    return redirect("student_login")

@login_required (login_url='login')
def student_home(request):
    student=StudentReg.objects.filter(StudentEmail=request.user.email).first()
    return render(request,'studenthomepage.html',{"student":student})


def applycourse(request):
    title="Course application Form"
    form=RegisterForm(request.POST,request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            F_name=form.cleaned_data['First_name']
            M_name= form.cleaned_data['Middle_name']
            L_name=form.cleaned_data['Last_name']
            mail=form.cleaned_data['Student_Email'] 
            ID=form.cleaned_data['ID_number']
            front=form.cleaned_data['frontID']
            # BCN=form.cleaned_data['Birthcertificatenumber']
            r_slip=form.cleaned_data['Results_Slip']        
            course=form.cleaned_data['course']
            user=User(email=mail,username=mail)
            user.save()
            p=StudentReg(user=user,Firstname=F_name,Middlename=M_name,Lastname=L_name,StudentEmail=mail,IDnumber=ID,ResultsSlip=r_slip,frontID=front,coursename=course)
            p.save()
            form=RegisterForm(request.POST,request.FILES or None)
            # messages.success(request,'Successefull Applied')
            return redirect('home')
        
        else:
            messages.error(request,"Fill all the fields")
            return redirect("applycourse/")
    else:
        context={
            "title":title,
            "form":form,
        }
    return render(request,'apply.html',context)

# @login_required (login_url='login')
def get_registration_no(course_code):
        Regnumber=f"{course_code}"# AC regnumber=AC
        two_n0=(ord(course_code[0])+ord(course_code[1]))%26
        r_no="".join([str(choice([1,2,3,4,5,6,7,8,9,0])) for _ in range(4)])
        Regnumber=f"{Regnumber}{two_n0}/{r_no}/2022"# regnumber= AC17/0756/2022
        return Regnumber
# @login_required (login_url='login')
def get_password(First_name):        
    return make_password(f"{First_name}1234")# password geofrey1234

# @login_required (login_url='login')
def get_student_email(StudentEmail,msg):
    send_mail(
        subject="Elgon View College",
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[StudentEmail])

@login_required (login_url='login')
def approve(request,student_id):
    student=StudentReg.objects.get(id=student_id)
    name=student.coursename
    course_code=Courses.objects.filter(course_name=name).first()
    student.status="APPROVED"
    student.save()
    user=User.objects.get(email=student.StudentEmail)
    Regnumber=get_registration_no(course_code.course_code)
    student.Regnumber=Regnumber
    student.save()
    user.username=Regnumber
    user.password=get_password(student.Firstname)    
    user.save() 
    msg= f"""
    with your application at Elgon view collage, 
    you have qualified for the course, 
    and you are required to go to our website and and access studentportal 
    and  login with username and and password, 
    thetreafter you are also required to make Update on your profile.
    Your Registration_no: {Regnumber},
    and your login credentials are:


    username: {Regnumber}, 
    password: {student.Firstname}1234. 
    """
    get_student_email(student.StudentEmail,msg)
    messages.success(request,f"{user.username} {user.password}")
    return redirect("registered_student")







@login_required (login_url='login')
def  Disapprove(request,student_id):
    applycourse=StudentReg.objects.get(id=student_id)
    applycourse.status='DISAPPROVED'
    applycourse.save()
    return redirect("registered_student")


@login_required (login_url='login')
def register(request):
    title="Student Registration Form"
    form=studForm(request.POST or None)
    if request.method == "POST":                  
        
        if form.is_valid():
                        
            T_number=form.cleaned_data['Telephonenumber']
            address=form.cleaned_data['Address']
            gender=form.cleaned_data['Gender']
            date=form.cleaned_data['DOB']                         
            s_photo=form.cleaned_data['photo']            
            # back=form.cleaned_data['backID']
            name=form.cleaned_data['Parent_name']
            email=form.cleaned_data['parent_email']
            number=form.cleaned_data['ParentTelephonenumber']            
            #print(Reg_number)  
            student=StudentReg.objects.filter(StudentEmail=request.user.email).first() 
            student.Telephonenumber=T_number
            student.Address=address
            student.Gender=gender
            student.DOB=date
            student.photo=s_photo
            student.Parent_name=name
            student.parent_email=email
            student.ParentTelephonenumber=number
            student.save()
            # messages.success(request,'Successefull Uploded')
        return redirect('student_home')
            
    else:
        context={
            "form":form,
        }
        
        messages.MessageFailure(request,'Registration Failed')
    return render(request,'reg.html',context)

@login_required (login_url='login')
def update_student_profile(request,Regnumber):
    student=StudentReg.objects.get(Regnumber=Regnumber)
    form=RegisterForm(instance=student)
    form=studForm(instance=student)
    if request.method=="POST":
        form=RegisterForm(request.POST,instance=student) 
        form=studForm(request.POST,instance=student)       
        if form.is_valid():
            form.save()
        return redirect("student")
    else:
        context={"form":form}
    return render(request,"reg.html",context)



# def profile(request):
#     title="Student Registration Form"
#     form=studprofile(request.POST or None)


#     if form.is_valid():
#         photo=form.cleaned_data['s_profile']
#         font=form.cleaned_data['front_Id']
#         back=form.cleaned_data['back_Id']
#         name=form.cleaned_data['parent_name']
#         email=form.cleaned_data['parent_email']
#         number=form.cleaned_data['parent_No.']         
#         p= StudentReg(s_profile=photo,front_Id=font,back_Id=back,parent_name=name,parent_email=email,parent_No=number)
#         p.save()
#         return redirect("/login_student/")
         
#     else:    

#      context={
#         "title":title,
#         "form":form,
#      }
#     return render(request,'profile.html',context)


@login_required (login_url='login')
def registered_student(request):
    title="Registered students"
    queryset=StudentReg.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context)


def approvedstudents(request):
    title="All students"
    queryset=StudentReg.objects.filter(status='APPROVED')
    form=searchform(request.POST or None)
    if request.method=="POST":
        form=searchform(request.POST or None)

        if form.is_valid():
            context={}
            form=searchform(request.POST or None)        
            # l_name=form.cleaned_data['Last_name']        
            register=form.cleaned_data['Regnumber']
            query=StudentReg.objects.filter(Regnumber=register).all()        
            if queryset is None:
                messages.info(request,f'Student not found')  
                         
            else:
                context={
                    
                "query":query,
                "form":form
                } 
            return render(request,'approvedstudents.html',context)

        else:
            
            messages.error(request,"invalid form")
        return render(request,'approvedstudents.html',{"form":form})
    else:
        context={
        "title":title,
        "form":form,
        "queryset":queryset, 
        }
    return render(request,'approvedstudents.html',context)


@login_required (login_url='login')
def update(request,user):
    student=StudentReg.objects.get(id=user)
    template=loader.get_templete("update.html")
    context={
        "student":student,
    }
    messages.success(request,"successfully updated")
    return redirect("/registered_student/")


@login_required (login_url='login')
def search(request):
    title="search student"
    form=searchform(request.POST or None)
    if form.is_valid():
        register=form.cleaned_data['Regnumber']
        # l_name=form.cleaned_data['Last_name']
        queryset=StudentReg.objects.filter(Regnumber=register)
        if len(queryset)==0:
            messages.info(request,'student not found')
            return redirect("/registered_student/")

        else:
                      
            context={
            "title":title,
            "queryset":queryset,
            }
        return redirect('/registered_student/',context)
    else:
     context={
        "title":title,
        "form":form, 
     }
    messages.error(request,'student not found')
    return redirect("/registered_student/")


# @login_required (login_url='login')
def delete(request,user):
    student=StudentReg.objects.get(user=user)
    if request.method=="POST":
        student.delete() 
       
        return redirect("approvedstudents")
    else:
         context={      
        "item":student
         }
    return render(request,'drop.html',context)
    # title="Delete"
    # form=StudentReg(request.POST or None)
    
    # if form.is_valid():
    #     reg=form.cleaned_data['id']
    #     queryset=StudentReg.object.filter(registration_number=user).delete()
    #     if len(queryset)==0:
    #         form=StudentReg(request.POST or None)
    #         return redirect(request,"existing.html",{"form":form})
    #     else:
    #         messages.success(request,"student deleted from your databse")
    #         return redirect(request,'existing.html') 

    # context={
    #     "title":title,
    #     "queryset":queryset,
    #      }
    # return render(request,'drop.html',context)

def studentspdf(request):
    student=StudentReg.objects.filter(status="APPROVED") 
    template_path='elgostudents.html'
    context={"student":student}
    response=HttpResponse(content_type='application/pdf')
    response['Content-DIsposition']="filename=students_report.pdf'"
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(
        html, dest=response
    )
   
    if pisa_status.err:
        return HttpResponse('we had some errors<pre>' + html + '</pre>')
    return response
        


def adminpage(request):
    return render(request,'admin.html')












    




    
    
    


