from django.urls import path
from payment import views

urlpatterns=[
 path('feespayment/',views.fees,name='feespayment'),
 path('searchstudentfees/',views.searchstudentfees,name='searchstudentfees'),
 path('feesstatement/',views.feesstatement,name='feesstatement'),
 path('callback/',views.callback,name='callback_url'),
 path('sem_fees/',views.semesterfees,name='sem_fees'),
 path('fees_stucture/',views.fees_stucture,name='fees_stucture'),
 path('update_semester_fees/<semester>',views.update_semester_fees,name='update_semester_fees'),
 path('update_student_fees/<id>',views.update_student_fees,name='update_student_fees'),
 path('userfees/',views.userfeesstatement,name='userfees'),
  path('studefeespdf/',views.studentfeesstatementpdf,name='studefeespdf'),
 ]