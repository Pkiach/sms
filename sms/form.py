from operator import truediv
from django import forms
from django.forms.widgets import NumberInput
from course.models import Courses 
from .models import StudentReg



# course_choices=[
#     ('Business Management', 'Business Management'),
#     ('Journalisim', 'Journalisim'),
#     ('ACCOUNTING AND FINANCE', 'ACCOUNTING AND FINANCE'),
#     ('INFORMATION AND COMMUNICATIONTECHNOLOGY', 'INFORMATION AND COMMUNICATIONTECHNOLOGY'),   
    
# ]


course_choices=[(course.course_name, course.course_name) for course in Courses.objects.all()]


class RegisterForm(forms.Form):     
     First_name=forms.CharField(max_length=26,widget=forms.TextInput(attrs={'placeholder': 'firstname no', 'style': 'width: 300px;'}))
     Middle_name= forms.CharField(max_length=26,widget=forms.TextInput(attrs={'placeholder': 'middle name', 'style': 'width: 300px;'}))
     Last_name=forms.CharField(max_length=26,widget=forms.TextInput(attrs={'placeholder': 'last name', 'style': 'width: 300px;'}))
     Student_Email=forms.EmailField(max_length=42,widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 300px;'}))
     ID_number=forms.CharField(max_length=9,widget=forms.TextInput(attrs={'placeholder': 'ID no', 'style': 'width: 300px;'}))
     Results_Slip=forms.ImageField(required=False)
     frontID=forms.ImageField(required=False)
     # Birthcertificatenumber=forms.ImageField(max_length=18,required=False)
         
     course=forms.ChoiceField(choices=course_choices)
     
     def save(self,commit=True):
          instance=super(RegisterForm,self).save(commit=False)
          if instance.approved:
               instance.status=1
               if commit:
                    instance.save()
                    return instance



gender_choice=[('Male','Male'),
('Female','Female'),
]

class studForm(forms.Form):         
     Telephonenumber=forms.CharField(max_length=16,required=True)
     Address=forms.CharField(max_length=36,required=True)     
     Gender=forms.ChoiceField(widget=forms.RadioSelect,choices=gender_choice,required=True)
     DOB=forms.DateField(widget=NumberInput(attrs={'type':'date'}))        
     photo=forms.ImageField(required=True)     
    #  backID=forms.ImageField(required=False)
     Parent_name=forms.CharField(max_length=40,required=True)  
     parent_email=forms.EmailField(max_length=36,required=True)
     ParentTelephonenumber=forms.CharField(max_length=14,required=True)        
     
       

class searchform(forms.Form):
     Regnumber=forms.CharField(max_length=14)
     # class Meta:
     #      model=StudentReg
     #      fields=['Regnumber']
            #  Last_name= forms.CharField(max_length=16)
          
