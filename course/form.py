from dataclasses import fields
from pyexpat import model
from django import forms
from django.conf import settings

from course.models import Department,Attendance,Courses
from course.models import SubjectRegistration


class courseform(forms.ModelForm):
    class Meta:
        model=Courses
        fields= ['course_code','course_name']

class Searchform(forms.Form):
    course_code=forms.CharField(max_length=8)

    
    
class searchdeptform(forms.Form):
    dept_code=forms.CharField(max_length=8)
  

class departmentform(forms.ModelForm):
    class Meta:
        model=Department
        fields= ['school_id','dept_code','department_name']
        # widgets = {
        #     'name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     'email': EmailInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email'
        #         })
        # }

  


class Subjectform(forms.Form):
    subjectcode=forms.CharField(max_length=10,)
    subject_name=forms.CharField(max_length=100)
    dept_no=forms.CharField(required=True)


class AttendanceForm(forms.ModelForm):
    # date=DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model=Attendance
        fields=['unit','present','date','start_time','end_time']
      


class StudentsttendanceForm(forms.ModelForm):
    # date=DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model=Attendance
        fields=['unit']
      

class SubjectRegistrationForm(forms.ModelForm):

    class Meta:
        model=SubjectRegistration
        fields=['student_id','subject','term_id'] 
        

# class Lecturer_SubjectsForm(forms.ModelForm):

#     class Meta:
#         model=Lecturer_Subjects
#         fields=['subjects','lecturer'] 
        
