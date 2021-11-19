from rest_framework import serializers
from .models import Students, StudentCourses
from schools_app.models import School

# from courses.models import Courses


class StudentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    date_of_birth = serializers.DateField()
    is_active = serializers.BooleanField()
    is_graduated = serializers.BooleanField()

    def __str__(self):
        return self.name


    def create(self, validated_data):
        student = Students.objects.create(**validated_data)
        return student

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.school=validated_data.get("school", instance.school)
    #     instance.date_of_birth=validated_data.get("date_of_birth", instance.date_of_birth)
    #     instance.is_active=validated_data.get("is_active", instance.is_active)
    #     instance.is_graduated=validated_data.get("is_gradueted", instance.is_graduated)
    #     instance.save()
    #     return instance


# class StudentCourses(serializers.Serializer):
#     student = serializers.PrimaryKeyRelatedField(queryset=Students.objects.all())
#     course = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())
#
#     def __str__(self):
#         return f'{self.student}, {self.course}'
