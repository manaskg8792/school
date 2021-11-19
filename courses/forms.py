
from django.forms import ModelForm
from django import forms
from .models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'school', 'is_active', 'price', 'duration', 'max_students']

# class CoursesForm(form.Form):
#     school = forms
