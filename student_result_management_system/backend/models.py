from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

def validate_age(value):
    if value > date.today() - relativedelta(years=10):
      raise ValidationError("Student must be at least 10 years old.")

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=120)
    family_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default=date.today, validators=[validate_age])
    email_address = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.family_name}"
    
class Course(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Score(models.Model):
    name = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.name
    
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course',)

    def __str__(self):
        return f"{self.student.first_name} {self.student.family_name}"