from xml.etree.ElementInclude import include
from django.urls import path
from sms import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about_us,name="about"),
    path('staff/',views.staff, name="staff"),
    path('contacts/',views.contacts,name="contacts"),
    path('students/',views.students,name="students"),
    path('applycourse/',views.applycourse,name="applycourse"),
    path('approve/<int:student_id>',views.approve,name="approve"),
    path('Disapprove/<int:student_id>',views.Disapprove,name="Disapprove"),
    path('register/',views.register,name="register"),
    path('student_home/',views.student_home,name="student_home"),
    path('registered_student/',views.registered_student,name="registered_student"),
    path('approvedstudents/',views.approvedstudents,name="approvedstudents"),
    path('search/',views.search,name="search"),
    path('delete/<int:user>',views.delete,name="delete"),
   # path('profile/',views.profile,name="profile"),    
    path('adminpage/',views.adminpage,name="adminpage"),
    path('studentspdf/',views.studentspdf,name="studentspdf"),
    path('students_pdf/',views.students_information,name="students_pdf"),



      
   
]