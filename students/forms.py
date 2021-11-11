from django.forms import ModelForm
from .models import Students
from .models import StudentCourse
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'school', 'date_of_birth', 'is_active', 'is_graduated']

class StudentCourse_form(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['student', 'course']