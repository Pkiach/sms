from django.urls import path
from staff import views

urlpatterns = [
    path('staffhome/',views.staffhome,name='staffhome'),
    path('staffinfo/',views.staffinformation,name='staffinfo'),
    path('delete_staff/<id>',views.delete_staff,name='delete_staff'),
    path('lectuer_class_attendance/',views.lectuer_class_attendance,name='lectuer_class_attendance'),
    path('registstaff/',views.registstaff,name='registstaff'),
    path('loginstaff/',views.login_staff,name='loginstaff'),
    path('logoutstaff/',views.logoutstaff,name='logoutstaff'),
    path('staffadmin/',views.staffadmin,name='staffadmin'),
    # path('adminlogin/',views.login_admin,name='adminlogin')
]