from django.shortcuts import render
from django.views import generic
from .models import School
from .forms import SchoolForm



class SchoolView(generic.CreateView):
    pass