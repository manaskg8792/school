from django.db import models
from django.core.validators import MaxValueValidator



class Courses(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey('schools_app.School',on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    duration = models.IntegerField()
    max_students = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20)])

    def __str__(self):
        return self.name
