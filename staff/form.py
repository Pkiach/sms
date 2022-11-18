from django import forms
from course.models import Subjects,Department


 
# subjectcode_choices=[
#    ('BM100', 'Business MANAGEMENT'),
#    ('CD100 ', 'Certificate in ECD'),
#    ('DA100 ', 'Diploma in Accounting')
# ]
TYPE_SELECT=[
    ('Male','Male'),
    ('Female','Female')]

status_choice=[
    ('Inactive','Inactive'),
    ('Active','Active')
]

departments_choices=[(department.dept_code, department.dept_code) for department in Department.objects.all()]
subjects_choices=[(subject.subjectcode, subject.subjectcode) for subject in Subjects.objects.all()]

class Lecturersform(forms.Form):
    # Lecturernumber=forms.CharField(max_length=20, label='Lecturer_Number',required=True)
    Title= forms.CharField(max_length=16,label='Title',required=True,widget=forms.TextInput(attrs={'placeholder': 'Mr', 'style': 'width: 300px;'}))
    Firstname=forms.CharField(max_length=34,label='First_Name',required=True,widget=forms.TextInput(attrs={'placeholder': 'First name', 'style': 'width: 300px;'}))
    Middlename=forms.CharField(max_length=30,label='Middle_Name',required=False,widget=forms.TextInput(attrs={'placeholder': 'Middle name', 'style': 'width: 300px;'}))
    Lastname=forms.CharField(max_length=30,label='Last_Name',required=True,widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style': 'width: 300px;'}))
    email=forms.EmailField(label='Email',required=True,widget=forms.TextInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;'}))
    telephonenumber=forms.CharField(max_length=22,label='Telephone_Number',required=True,widget=forms.TextInput(attrs={'placeholder': 'Telephone no', 'style': 'width: 300px;'}))
    address=forms.CharField(max_length=40,label='Address',required=True,widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 300px;'}))
    Gender=forms.ChoiceField(widget=forms.RadioSelect,choices=TYPE_SELECT)
    IDnumber=forms.CharField(max_length=15,label='ID_Number',required=True,widget=forms.TextInput(attrs={'placeholder': 'ID no', 'style': 'width: 300px;'}))
    department=forms.ChoiceField(choices=departments_choices,label='Department_code')
    subjects=forms.ChoiceField(choices=subjects_choices,label='subject_code')
    # status=forms.ChoiceField(choices=status_choice)



class adminform(forms.Form):
    Title= forms.CharField(max_length=16,widget=forms.TextInput(attrs={'placeholder': 'Mr', 'style': 'width: 120px;;'}))
    Firstname=forms.CharField(max_length=34,widget=forms.TextInput(attrs={'placeholder': 'First name', 'style': 'width: 120px;'}))
    Middlename=forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': 'First name', 'style': 'width: 120px;'}))
    Lastname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style': 'width: 120px;'}))
    Email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'style': 'width: 120px;'}))
    Telephonenumber=forms.CharField(max_length=22,widget=forms.TextInput(attrs={'placeholder': 'Telephone no', 'style': 'width: 120px;'}))
    Address=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 120px;'}))
    Gender=forms.CharField(max_length=15,widget=forms.RadioSelect(choices=TYPE_SELECT))
    IDnumber=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'ID no', 'style': 'width: 120px;'}))
    status=forms.ChoiceField(choices=status_choice)
    
    

class Loginstaffform(forms.Form):
    username=forms.CharField(max_length=26,required=True)
    password= forms.CharField(min_length=7,widget=forms.PasswordInput)