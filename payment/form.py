from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms

from .models import Payment, Semesterfees


class FeesdataForm(forms.ModelForm):
    class Meta:
        fields= all

class PaymentForm(forms.ModelForm):

      class Meta:
        model = Payment
     

        fields=['telephone_number','amount_paid']
       
        # extra_kwargs = {
        #     'telephone_number':{
        #         'type': int
        #     }
        # }



SEMESTER_CHOICES=(
    ('', 'selelect semsester'),
    ('1', '1'),
    ('2','2'))
widget={'semester':forms.Select(choices=SEMESTER_CHOICES)}



STATUS_CHOICES=(
    ('', 'selelect semsester'),
    ('Inactive', 'Inactive'),
    ('Current','current'))
widget={'status':forms.Select(choices=STATUS_CHOICES)}


class feesForm(forms.ModelForm):
    semester = forms.ChoiceField(
        widget=forms.Select,
        choices=SEMESTER_CHOICES
    )

    status = forms.ChoiceField(
        widget=forms.Select,
        choices=STATUS_CHOICES
    )
    class Meta:
        model=Semesterfees
        fields=['semester','fees','year','status']

    # SEMESTER_CHOICES=(
    #     ('', 'selelect semsester'),
    #     ('1', '1'),
    #     ('2','2'))
    # widget={'semester':forms.Select(choices=SEMESTER_CHOICES)}

    # STATUS_CHOICES=(
    #     ('', 'selelect status'),
    #     ('False', 'False'),
    #     ('Current','Current'))
    # widget={'status':forms.Select(choices=STATUS_CHOICES)}
    
    


    
class Searchfeesform(forms.ModelForm):

    class Meta:
        model=Payment
        fields=['student_number']
        exclude=['amount_paid','phone_number']