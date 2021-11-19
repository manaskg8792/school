from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, status, parsers, response

from .models import Students
from .serializers import StudentsSerializer


@csrf_exempt
def student_list(request):
    if request.method == "GET":
        students = Students.objects.all()
        serializer = StudentsSerializer(instance=students, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        data = parsers.JSONParser().parse(request)
        serializer = StudentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def student_detail(request, pk):
    try:
        students = Students.objects.get(id=pk)
    except Students.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = StudentsSerializer(instance=students)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method in {'PUT', 'PATCH'}:
        data = parsers.JSONParser().parse(request)
        serializer = StudentsSerializer(instance=students, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        students.delete()
        return HttpResponse(204)


class StudentListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        students = Students.objects.all()
        serializer = StudentsSerializer(instance=students, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):
    def get_object(self, pk):
        try:
            students = Students.objects.get(id=pk)
        except Students.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, pk, request, *args, **kwargs):
        students = self.get_object(pk)
        serializer = StudentsSerializer(instance=students, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        students = self.get_object(pk)
        data = parsers.JSONParser().parse(request)
        serializer = StudentsSerializer(instance=students, data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data, status=200)

        return response.Response(serializer.errors, status=400)

    def delete(self, request, pk):
        students = self.get_object(pk)
        students.delete()
        return response.Response(204)












#
# class StudentCreateView(generic.CreateView):
#     model = Students
#     form_class = StudentForm
#     template_name = 'students.html'
#     success_url = '/students/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['students'] = Students.objects.all()
#         return context
#
#
# class StudentCoursesView(generic.CreateView):
#     model = StudentCourses
#     form_class = StudentCoursesForm
#     template_name = 'studentcourse.html'
#     success_url = '/students/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['studentcourses'] = StudentCourses.objects.all()
#         return context








