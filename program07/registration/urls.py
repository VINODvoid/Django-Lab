from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
]
