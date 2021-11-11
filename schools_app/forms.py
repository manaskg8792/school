from django.forms import ModelForm
from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address']