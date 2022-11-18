
from django.urls import path
from course import views

urlpatterns=[
 path('course/',views.courseoffered,name='course'),
 path('elgoncourses/',views.courses,name='elgoncourses'),
 path('coursereg/',views.regcourse,name='coursereg'),
  path('update_course/<course_code>',views.update_course,name='update_course'),
 path('offered/',views.searchcourse,name='offered'),
 path('add/',views.addsubject,name='add'),
 path('subjects/',views.subjects,name='subjects'),
 path('update_subject/<subjectcode>',views.update_subject,name='update_subject'),
 path('drop/<subjectcode>',views.remove_subject,name='drop_subject'),
 path('searchcourse/',views.searchcourse,name='searchcourse'),
 path('delcos/<course_code>',views.deletecourse,name='delcos'),
 path('adddepartment/',views.adddepartment,name='adddepartment'),
 path('departments/',views.departments,name='departments'),
 path('update_department/<dept_code>',views.update_department,name='update_department'),
 path('remove/<dept_code>',views.delete_department,name='remove'),
 path('attendance/',views.attendance,name='attendance'),
 path('studentattendance/',views.studentattendance,name='studentattendance'),
 path('update_class_attendance/<student_id>',views.update_class_attendance,name='update_class_attendance'),
 path('class_list/',views.list_ofclass_attendance,name='class_list'),
 path('registersubject/',views.subregistration,name='registersubject'),
 path('units/',views.registeredsubject,name='units'),
 path('assigned/',views.subjects_registered,name='assigned'),
#   path('subject_assigning_update/<assigning_id>',views.subject_assigning_update,name='subject_assigning_update'),
#  path('assign_lecturer_subjects/',views.assign_lecturer_subjects,name='assign_lecturer_subjects'),
 

 

]