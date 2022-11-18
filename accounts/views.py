from email import message
from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from.form import Loginform




 

# @login_required (login_url='login')
def student_login(request):
    form=Loginform()
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():  
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.filter(username=username).first()
            if user and check_password(password,user.password):                 
                login(request,user)
                # messages.error(request,f'User Logged In {user.username}')
                # redirect to the next page
                return  redirect("student_home")
            else:
                #either username or passaword is incorrect
                messages.error(request,'Invalid username or password')           
                form=Loginform()
                return redirect("student_login")                
        else:
            messages.error(request,f'Form is not valid {form.cleaned_data}')     
    context={        
        "form": form
        }
    return render(request,'accounts/signin_students.html',context) 


# @login_required (login_url='logout')
def logoutstudent(request):
    logout(request)
    return redirect('home')

# # # @login_required (login_url='login')
# # # def fees(request):
# # #     return render(request,"paynent.html",name=fees)


# # @login_required (login_url='login')
def login_staff(request):
    title="Staff login"
    msg=None
    form=AuthenticationForm(data=request.POST) 
          
    if form.is_valid(): 
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None and User.is_admin:
            login(request,user)
            return redirect("{% url 'staffadmin' %}")

        elif user is not None and User.is_lecturer:
            login(request,user)
            return redirect("{% url 'staffhome' %}")

        else:
            msg="Invalid username or password "
            return render(request,"accounts/signin.html")
    else:
        context={
            "tittle":title,
            "form":form,
            "msg":msg
            }
        return render(request,"accounts/signin.html",context)



# def signUp(request):
#     title="SignUp Form"
#     msg=None
#     form=SignUpform(request.POST)
#     if request.method=="POST":
        
#         if form.is_valid():
#             user=form.saved()
#             msg="User created"
#             return redirect("/signin/")

#         else:
#             msg='Form is not valid'

#     else:
#         context={
#             "title":title,
#             "form": form,
#         }   
#         return render(request,"accounts/signup.html",context)



    





