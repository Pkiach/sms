
# from django import forms
from django import forms
from django.contrib.auth.models import User





class Loginform(forms.Form):
    username=forms.CharField(max_length=26,required=True)
    password= forms.CharField(min_length=7,widget=forms.PasswordInput)
    

    
# class SignUpform(forms.ModelForm):
#     #  username=forms.CharField(Widget=forms.TextInput(attrs={
#     #       # "class":"form_control"
#     #  }
#     #  ))

#     #  email=forms.EmailField(Widget=forms.TextInput(attrs={
#     #            # "class":"form_control"
#     #       }
#     #       ))

#     #  password1=forms.PasswordInput(Widget=forms.PasswordInput(attrs={
#     #       # "class":"form_control"
#     #  }
#     #  ))

#     #  password2=forms.PasswordInput(Widget=forms.PasswordInput(attrs={
#     #       # "class":"form_control"
#     #  }
#     #  ))

    


#      class Meta:
#           model=User
#           fields=['username',"email","password1","passwrd2","is_admin","is_staff","is_student"]