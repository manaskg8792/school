from django.urls import path
from .views import student_list, student_detail, StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail',)
    # path('', views.StudentCreateView.as_view()),
    # path('course/', views.StudentCoursesView.as_view())
]