from django.shortcuts import render, redirect
from .models import Student, Course, Enrollment
from .forms import StudentForm, EnrollmentForm, CourseForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'registration/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'registration/course_list.html', {'courses': courses})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = EnrollmentForm()
    return render(request, 'registration/enroll_student.html', {'form': form})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    return render(request, 'registration/course_detail.html', {'course': course, 'enrollments': enrollments})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'registration/add_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'registration/add_course.html', {'form': form})
