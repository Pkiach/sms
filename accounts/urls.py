from django.urls import path
from accounts import views

urlpatterns=[
    # path('login/',views.login_staff,name='login'),
     path('logoutstudent/',views.logoutstudent,name='logoutstudent'),
     path('login_staff/',views.login_staff,name='login_staff'),
     path('student_login/',views.student_login,name='student_login'),
    #    path("signUp/",views.signUp,name="signUp"),
    # path("signin/",views.login,name="signin"),
    # path('logout/',views.logoutuser,name='lougout'),
    
 ]