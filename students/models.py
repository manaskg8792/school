from django.db import models




class Students(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey('schools_app.School', on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    is_active = models.BooleanField()
    is_graduated = models.BooleanField()

    def __str__(self):
        return self.name


class StudentCourses(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Courses', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.student}, {self.course}'



