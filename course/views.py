from binascii import Incomplete
import code
from email import message
from multiprocessing import context
from tkinter import Y
from turtle import title
from urllib import request
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from payment.models import Payment,Semesterfees
from .models import Attendance, Courses, Department, Subjects,SubjectRegistration
from .form import Subjectform, courseform, departmentform,AttendanceForm,SubjectRegistrationForm,StudentsttendanceForm,Searchform,searchdeptform
from django.contrib import messages
from staff.models import Lecturers
from sms.models import StudentReg

from course import form




def registersubject(request):
    title="Subject Registration"
    form=SubjectRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'successfull RegIstered')
            return redirect("/students/")

        else:
            messages.error(request,"Registration Failed")
            return render(request,"course/unitregistration.html")
            
    else:
        context={
            "form":form
        }
        return render(request,"course/unitregistration.html",context)



# @login_required (login_url='login')

def attendance(request):
    title="Class attendance"
    # name=Lecturers.objects.filter('Firstname')
    form=AttendanceForm()
    if request.method == "POST":
        if form.is_valid():
            sign=get_object_or_404(Attendance,created_by=request.StudentReg)  
            sign.present=1
            sign.save(update_fields=['present'])
            messages.success(request,'successfully submited')
            return render(request,'course/attendance.html')
        else:
            sign.present=0
            sign.save(update_fields=['present'])
            messages.error(request,'You are absent,you are not in class!!')
        return render(request,'course/attendance.html')
    else:
        context={
            "title":title,
            "form":form,
        }
    messages.success(request,'Submition Failed')
    return render(request,'course/attendance.html',context)

def list_ofclass_attendance(request):
    title="class attendance"
    queryset=Attendance.objects.filter(present=1)

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render("request,'course/classattendance.html',context",context)



def studentattendance(request):
    title="Class attendance"
    # name=Lecturers.objects.filter('Firstname')
    student=StudentReg.objects.filter(StudentEmail=request.user.email).first()
    # reg_no=student.Regnumber
    form=StudentsttendanceForm()
    if request.method == "POST":
        if form.is_valid():
            sign=get_object_or_404(Attendance,created_by=request.student)  
            sign.present=1
            sign.save(update_fields=['present'])
            messages.success(request,'successfully submited')
            return render(request,'course/studentattendance.html')
        else:
            sign.present=0
            sign.save(update_fields=['present'])
            messages.error(request,'You are absent,you are not in class!!')
        return render(request,'course/studentattendance.html')
    else:
        context={
            "title":title,
            "form":form,
        }
    messages.success(request,'Submition Failed')
    return render(request,'course/studentattendance.html',context)

def list_ofclass_attendance(request):
    title="class attendance"
    queryset=Attendance.objects.filter(present=1)

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render("request,'course/classattendance.html',context",context)


def update_class_attendance(request,student_id):
    student=Attendance.objects.get(student_id=student_id)
    form=AttendanceForm(instance=student_id)
    if request.method=="POST":
        form=AttendanceForm(request.POST,instance=student)       
        if form.is_valid():
            form.save()
        return redirect("class_list")
    else:
        context={"form":form}
    return render(request,"course/attendance.html",context)



@login_required (login_url='login')
def regcourse(request):
    title="Add course"
    form=courseform(request.POST or None)
    if request.method == "POST":       
        if form.is_valid():
            
            form.save()
            messages.success(request,"course registered")
            return redirect("course")
        else:
            messages.error(request,'Registration failed')
        return render(request,'course/coursereg.html')
    else:        
        context={
            "title":title,
            "form":form,
        }
    return render(request,'course/coursereg.html',context)


def courses(request):
   
   
    return render(request,"course/courses.html")

@login_required (login_url='login')
def courseoffered(request):
    title="Courses offered in ELGON VIEW COLLEGE"
    queryset=Courses.objects.filter()
    # .order_by("course_code")
    form=Searchform()
    if request.method=="POST":
        form=Searchform(request.POST or None)
        if form.is_valid():
            context={}
            form=Searchform(request.POST or None)
            code=form.data['course_code']
            query=Courses.objects.filter(course_code=code)
            if len(query)==0:
                messages.info(request,f'course not found')           
            else:
                context={
                
                "queryset":query,
                "form":form
                } 
            return render(request,'course/offeredcourse.html',context)

        else:
            
            messages.error(request,"invalid form")
        return render(request,'course/offeredcourse.html')

    else:

        context={
        "title":title,
        "queryset":queryset,
        "form":form 
        }
    return render(request,'course/offeredcourse.html',context)


@login_required (login_url='login')
def update_course(request,course_code):
    course=Courses.objects.get(course_code=course_code)
    form=courseform(instance=course)
    if request.method=="POST":
        form=courseform(request.POST,instance=course)         
        if form.is_valid():
            form.save()
            return redirect("course")
        else:
            messages.error(request,'Not updated')
        return render(request,"course/coursereg.html",{"form":form})
    else:
        context={"form":form}
    return render(request,"course/coursereg.html",context)

def searchcourse(request):
    title="search course"
    form=Searchform()
    if request.method=="POST":
        form=Searchform(request.POST or None)
        if form.is_valid():
            code=form.cleaned_data['course_code']
            queryset=Courses.objects.filter(course_code=code)
            if len(queryset)==0:
                messages.info(request,'course not found')           

            else:
                context={
            
            "queryset":queryset,
            }
            messages.success(context)

    else:
        context={
        "title":title,
         "form":form,
         }
    return render(request,'course/offeredcourse.html',context)

    
def deletecourse(request,course_code):
    course=Courses.objects.get(course_code=course_code)
    if request.method=="POST":
        course.delete()       
        return redirect('course' ) 
    else:
        context={      
        "item":course,
         }
    return render(request,'course/drop.html',context)

@login_required (login_url='login')
def addsubject(request):    
    title="Add Subject"
    form=Subjectform(request.POST or None)
    if request.method == "POST": 
        if form.is_valid():
            code=form.cleaned_data['subjectcode']
            name=form.cleaned_data['subject_name']
            no=form.cleaned_data['dept_no']
            sub=Subjects.objects.filter(subjectcode='sub')
            dept=Department.objects.filter(dept_code=no).first()
            if len(sub)>0:
                messages.error(request,"Subject Already Exist") 
            else:
                p=Subjects(subjectcode=code,subject_name=name,dept_no=dept)
                p.save()
                messages.success(request,'successfully registered')
            return redirect("subjects")
    else:

        context={
            'title':title,
            'form':form,
            }
        return render(request,'course/addsubject.html',context)


def subjects(request):
    title="All subjects"
    queryset=Subjects.objects.all().order_by("subjectcode")

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render(request,'course/allsubjects.html',context)



def update_subject(request,subjectcode):
    subject=Subjects.objects.get(subjectcode=subjectcode)
    form=Subjectform(instance=subject)
    if request.method=="POST":
        form=Subjectform(request.POST, instance=subject)       
        if form.is_valid():
            form.save() 
        return redirect("subjects")
    else:
        context={"form":form}
    return render(request,"course/addsubject.html", context)


   
def remove_subject(request,subjectcode):
    subject=Subjects.objects.get(subjectcode=subjectcode)
    if request.method=="POST":
        subject.delete()       
        return redirect("subjects")
    else:
         context={      
        "item":subject
         }
    return render(request,'course/deletesubject.html',context)


def adddepartment(request):
    title="Add department"
    form=departmentform(request.POST or None)
    if request.method == "POST":        
        if form.is_valid():
            school=form.cleaned_data['school_id']
            dept=form.cleaned_data['dept_code']
            deptname=form.cleaned_data['department_name']
            no=Department.objects.filter(dept_code=dept)
            if len(no)>0:
             messages.error(request,"Department Already Exist") 
            else:
                p=Department(school_id=school,dept_code=dept,department_name=deptname)
                p.save()
                messages.success(request,'successfully registered')
            return redirect("departments")

        else:
            messages.error(request,'Registration failed')
        return render(request,"course/add.html")
    else:
        context={            
            'title':title,
            'form':form,
        }
    return render(request,'course/add.html',context)



def departments(request):
    title="Departments in ELGON VIEW COLLEGE"
    queryset=Department.objects.all().order_by("school_id")
    form=searchdeptform()
    if request.method=="POST":
        form=searchdeptform(request.POST or None)
        if form.is_valid():
            context={}
            form=searchdeptform(request.POST or None)
            dept=form.data['dept_code']
            query=Department.objects.filter(dept_code=dept).all()
            if query is None:
                # messages.info(request,f'Department not found')  
                pass         
            else:
                context={
                
                "queryset":query,
                "form":form
                } 
            return render(request,'course/department.html',context)

        else:
            
            messages.error(request,"invalid form")
        return render(request,'course/department.html',{"form":form})

    context={
    "title":title,
    "form":form,
    "queryset":queryset, 
    }
    return render(request,'course/department.html',context)




def update_department(request,dept_code):
    department=Department.objects.get(dept_code=dept_code)
    form=departmentform(instance=department)
    if request.method=="POST":
        form=departmentform(request.POST,instance=department)       
        if form.is_valid():
            form.save()
        return redirect("departments")
    else:
        context={"form":form}
    return render(request,"course/add.html",context)


def delete_department(request,dept_code):   
    department=Department.objects.get(dept_code=dept_code)
    if request.method=="POST":
        department.delete() 
       
        return redirect("departments")
    else:
         context={      
        "item":department
         }
    return render(request,'course/remove.html',context)
    
    


# def getsum(payment_objects):
#     amount=0
#     for payment_object in payment_objects:
#         amount+=payment_object.amount_paid
#     return amount
    

def subregistration(request):
    title="Subject Registration"
    form=SubjectRegistrationForm(request.POST or None)
    reg=StudentReg.objects.filter(StudentEmail=request.user.email).first()
    if request.method=="POST":
        if request.user.is_authenticated:
            if form.is_valid(): 
               
                number=StudentReg.objects.get(Regnumber=request.user.username)
                sem=form.cleaned_data["term_id"]                      
                queryset=Payment.objects.get(student_number=number)
                fees=Semesterfees.objects.get(semester=sem)
                form.save()   
                return redirect("registered")                    
                
        else:
            messages.error(request,"Subject registration failed")  
        return render(request,"course/registersub.html") 

    else:
        context={
            "title":title,
            "form":form,
        }  
        messages.error(request,"Subject registration failed")
    return render(request,"course/registersub.html",context)  

def subjects_registered(request):
    title="Registered Subjects"
    queryset=SubjectRegistration.objects.all().order_by("registration_id")

    context={
        "title":title,
        "queryset":queryset,        
    }
    return render (request,"course/registeredsubject.html",context)



def registeredsubject(request):
    title="Registered Subjects"
    unit=Lecturer_Subjects.objects.all()

    context={
        "title":title,
        "unit":unit,        
    }
    return render (request,"course/assignedsubject.html",context)


# def assign_lecturer_subjects(request):
#     title="Assigning subjects"
#     form=Lecturer_SubjectsForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("assigned")
#     else:
#         context={
#             "title":title,
#             "form":form
#         }
#         message.error(request,"subjectassigning.html")
#     return render(request,'course/subjectassigning.html',context)



# def subject_assigning_update(request,assigning_id):
#     assign=SubjectRegistration.objects.get(assigning_id=assigning_id)
#     form=Lecturer_SubjectsForm(instance=assign)
#     if request.method=="POST":
#         form=Lecturer_SubjectsForm(request.POST,instance=assign)       
#         if form.is_valid():
#             form.save()
#         return redirect("assigned")
#     else:
#         context={"form":form}
#     return render(request,"course/subjectassigning.html",context)


               



            

