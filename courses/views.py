from django.http import JsonResponse, HttpResponse
from django.views import generic
from rest_framework import views, status, parsers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.templatetags.rest_framework import data

from .models import Courses
from .serializers import CourseSerializer
from .forms import CourseForm

"""
    SSR - Server Side Rendering
    SPA - Single Page Application 
    
    REST - Representational state transfer
    
    methods = GET, POST, PUT, PATCH, DELETE
    /courses/
"""

@csrf_exempt
def courses_list(request):
    """
    List all courses or create a new course

    """
    if request.method == "GET":
        courses = Courses.objects.all()
        serializer = CourseSerializer(instance=courses, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def courses_detail(request, pk):
    """
    Retrieve, update or delete a course

    """
    try:
        course = Courses.objects.get(id=pk)
    except Courses.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(instance=course)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method in {'PUT', 'PATCH'}:
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializer(instance=course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(204)

        # serializer = CourseSerializer()


class CousreApiView(views.APIView):
    pass



class CourseCreateView(generic.CreateView):
    model = Courses
    form_class = CourseForm
    template_name = 'course.html'
    success_url = 'home'


