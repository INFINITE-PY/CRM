from django import forms
from .models import Group, Student, Grade, Subject, Author, Book, Course, Enrollment, Teacher

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'group']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'author']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'price']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'salary'] 