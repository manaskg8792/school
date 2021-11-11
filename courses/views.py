from django.views import generic
from .models import Courses
from .forms import CourseForm


class CourseCreateView(generic.CreateView):
    model = Courses
    form_class = CourseForm
    template_name = 'course.html'
    success_url = 'home'


