from django.urls import path
from .views import courses_list, courses_detail

urlpatterns = [
    # path('create/', CourseCreateView.as_view()),
    path('courses/', courses_list, name='courses_list'),
    path('courses/<int:pk>/', courses_detail, name='course-detail',)

]
