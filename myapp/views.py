from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Sum
from .models import Student, Grade, Author, Group, Teacher, Course
from .forms import StudentForm, GradeForm, AuthorForm, GroupForm, CourseForm, TeacherForm

def index(request):
    return render(request, 'index.html')

def task1(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task1')
    else:
        form = StudentForm()
    students = Student.objects.select_related('group').all()
    return render(request, 'task1.html', {'students': students, 'form': form})

def task2(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task2')
    else:
        form = GradeForm()

    grades = Grade.objects.select_related('student', 'subject').all()
    return render(request, 'task2.html', {'grades': grades, 'form': form})

def task3(request):
    students = Student.objects.prefetch_related('grades').all()
    return render(request, 'task3.html', {'students': students})

def task4(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task4')
    else:
        form = AuthorForm()

    authors = Author.objects.prefetch_related('books').all()
    return render(request, 'task4.html', {'authors': authors, 'form': form})

def task5(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task5')
    else:
        form = GroupForm()

    groups = Group.objects.annotate(student_count=Count('students'))
    return render(request, 'task5.html', {'groups': groups, 'form': form})

def task6(request):
    students = Student.objects.annotate(avg_score=Avg('grades__score'))
    return render(request, 'task6.html', {'students': students})

def task7(request):
    authors = Author.objects.annotate(book_count=Count('books'))
    return render(request, 'task7.html', {'authors': authors})

def task8(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task8')
    else:
        form = CourseForm()

    courses = Course.objects.annotate(enrollment_count=Count('enrollments'))
    return render(request, 'task8.html', {'courses': courses, 'form': form})

def task9(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task9')
    else:
        form = TeacherForm()

    data = Teacher.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'task9.html', {'avg_salary': data['avg_salary'], 'form': form})

def task10(request):
    data = Course.objects.aggregate(total_price=Sum('price'))
    return render(request, 'task10.html', {'total_price': data['total_price']})