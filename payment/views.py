
from email import message
from multiprocessing import context
from django.contrib import messages
from re import X
from django.shortcuts import redirect, render
from  sms.models import StudentReg
from django.http import HttpResponse

from .models import Payment,Semesterfees, Feesdata
from . form import PaymentForm,Searchfeesform,feesForm,FeesdataForm
from .utils import pay
from payment import form
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
from xhtml2pdf import pisa
# import socket
# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind("localhost", 8000)

# server.listen()

# Create your views here.


def studentfeesstatementpdf(request):
    student=Payment.objocts.filter (user=request.user).get() 
    template_path='studefeespdf.html'
    context={"student":student}
    response=HttpResponse(content_type='application/pdf')
    response['Content-DIsposition']="filename=studentsfees_report.pdf'"
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(
        html, dest=response
    )
   
    if pisa_status.err:
        return HttpResponse('we had some errors<pre>' + html + '</pre>')
    return response
        
def callback(request):
    if request.method == "POST":
        print(request.json) 

@login_required (login_url='login')
def fees(request):
    title="Fees Pament"
    form=PaymentForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid(): 
                      
            student=StudentReg.objects.get(user=request.user)
            
        
            phone =form.cleaned_data["telephone_number"]
            amount=form.cleaned_data["amount_paid"]
            resp=pay(phone_number=phone,amount=amount)
            print(resp)
            # state=Semesterfees.objects.filter(status='current')
            # sem_fees=Semesterfees.objects.filter(amount="amount").first()
            # total=getsum(amount)
            # balance=total-sem_fees
            # if balance>0 and state:
            #     student.stutus="INCOMPLETE"
            # form.save()
            # if balance<0 and state:
            #     student.status="COMPLETE"
            # form.save()
            payment_record = Payment(student_number=student
            ,telephone_number= form.data.get('telephone_number'), 
            amount_paid=form.data.get("amount_paid") )
            payment_record.save()

            sem=Semesterfees.objects.filter(status="Current").first()
            # Find the student in the fee data table by active term and student id
            fee_record_inserted = Feesdata.objects.filter(student_id=student, semester_id=sem).first()
            amount = int(form.data.get('amount_paid'))
            if fee_record_inserted is None:
                               
                status = ""
                if amount >= sem.fees:
                    status = "Complete"
             
                else:
                    status = "Incomplete"
                
                Feesdata(student_id=student, semester_id=sem,amount=amount, status=status).save()
            else:
                # over_payment = 0
                total_payment = fee_record_inserted.amount + int(amount) 
                status = ""
                if total_payment >= sem.fees:
                    status="Complete"
                # elif total_payment > sem.fees:
                #     over_payment = sem.fees - total_payment
                #     status="Complete"
                else:
                    status="Incomplete"             
               

                fee_record_inserted.amount=total_payment
                fee_record_inserted.status=status
                fee_record_inserted.save()
            # messages.success(request,'payment completed')
            return redirect("student_home")
        else:
            messages.error(request,'payment not completed')
        return render(request,'payment/payment.html')
            

    else:
        context={
            'title':title,
            'form':form,
        }
        
    return render(request,'payment/payment.html',context)


# def update_student_fees(Regnumber):   
#     subject=Courses.objects.get(subjectcode=subjectcode)
#     form=Subjects(instance=subject)
#     if request.method=="POST":
#         form=courseform(request.POST,instance=subject)
#         if form.is_valid():
#             form.save()
#         return redirect("subjects")

#         # context={"form":form}
#     return redirect("add")

@login_required (login_url='login')
def semesterfees(request):
    title="Fees Amount"
    form=feesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # messages.success(request,'successfull Updated')
            return redirect("fees_stucture")

        else:
            form=feesForm(request.POST or None)
            messages.error(request,"failed to update")
        return render(request,"payment/semfees.html",{"form":form})
            
    else:
        context={
            "title":title,
            "form":form
        }
        messages.error(request,"Doesn't to update")
    return render(request,"payment/semfees.html",context)

@login_required (login_url='login')
def fees_stucture(request):
    title="Fees structure"
    queryset=Semesterfees.objects.all()

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render(request,'payment/feesstucture.html',context)


@login_required (login_url='login')
def update_semester_fees(request,semester):
    term=Semesterfees.objects.get(semester=semester)
    form=feesForm(instance=term)
    if request.method=="POST":
        form=feesForm(request.POST,instance=term)
        if form.is_valid():
            form.save()
            messages.success(request,"payment updated")
            return redirect("fees_stucture")
        else:
            messages.error(request,"Not updated")
            return render(request,"payment/semfees.html")

    else:
        context={
            "form":form,
        }
    return render(request,"payment/semfees.html",context)

@login_required (login_url='login')
def update_student_fees(request,Regnumber):
    fees=Payment.objects.get(payment_code=Regnumber)
    form=PaymentForm(instance=fees)
    if request.method=="POST":
        form=PaymentForm(request.POST,instance=fees)        
        if form.is_valid():
            form.save()
            messages.success(request,"payment updated")
            return redirect("payment/feesstatement")
        else:
            messages.error(request,"Not updated")
            return render(request,"payment/payment.html")

    else:
        context={
            "form":form,
        }
    return render(request,"payment/payment.html",context)
    


def callback(request):
    if request.method == "POST":
        print(request.json) 

@login_required (login_url='login')
def userfeesstatement(request):
    title="Students payment"
    logged_student = StudentReg.objects.filter(user=request.user).get()
    queryset=Payment.objects.filter(student_number=logged_student).all()
    print(queryset)

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render(request,'payment/userfeesstatement.html',context) 
@login_required (login_url='login')
def feesstatement(request):
    title="Students payment"
    queryset=Payment.objects.all()

    context={
    "title":title,
    "queryset":queryset, 
    }
    return render(request,'payment/studentspayment.html',context)

@login_required (login_url='login')
def searchstudentfees(request):
    title="search student"
    form=Searchfeesform(request.POST or None)
    if form.is_valid():
        X=form.cleaned_data['student_registration']
        queryset=Payment.objects.filter(student_registration=X)
        if len(queryset)==0:
            
            return render(request,"payment/feessearch.html")

        else:
            messages.success(request,'student not found')

    
        context={
        "title":title,
        "queryset":queryset,
         }
        messages.sucess(request,"payment/feessearch.html",context)
    else:
     context={
        "title":title,
        "form":form, 
     }
     return render(request,'payment/feessearch.html',context)



def getsum(payment_objects):
    amount=0
    for payment_object in payment_objects:
        amount+=payment_object.amount_paid
    return amount

# @login_required (login_url='login')
# def feesdatabase(request):
#     form=FeesdataForm(request.POST or None) 
#     if form.method=="POST":
#         state=Semesterfees.objects.filter(status='current')
#         sem_fees=Semesterfees.objects.filter(amount="amount").first()
#         sum=form.cleaned_data["amount"]
#         total=getsum(amount)
#         balance=total-sem_fees
#         if balance>0 and state:
#             student.stutus="INCOMPLETE"
#             form.save()
#             if balance<0 and state:
#                 student.status="COMPLETE"
#     return render(request,'payment/feesdata.html')





