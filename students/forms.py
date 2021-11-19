from django.forms import ModelForm
from .models import Students
from .models import StudentCourses
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'school', 'date_of_birth', 'is_active', 'is_graduated']


class StudentCoursesForm(forms.ModelForm):
    class Meta:
        model = StudentCourses
        fields = ['student', 'course']