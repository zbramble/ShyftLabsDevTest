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
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = ('id', 'student_name', 'course_name', 'score')
    
    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.family_name}"
    
    def get_course_name(self, obj):
        return f"{obj.course.name}"
    
    def get_score(self, obj):
        return f"{obj.score.name}"