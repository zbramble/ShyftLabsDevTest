from rest_framework import serializers
from .models import Student
from .models import Course
from .models import Result
from .models import Score

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'family_name', 'date_of_birth', 'email_address')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'name')

class ResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    score = ScoreSerializer(read_only=True)

    class Meta:
        model = Result
        fields = ('id', 'student', 'course', 'score')