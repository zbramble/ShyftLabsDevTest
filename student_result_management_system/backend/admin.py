from django.contrib import admin
from .models import Student
from .models import Course
from .models import Result
from .models import Score

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'family_name', 'date_of_birth', 'email_address')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course_name', 'score')
    
    def student_name(self, instance):
        return f"{instance.student.first_name} {instance.student.family_name}"
    
    def course_name(self, instance):
        return instance.course.name
    
    def score(self, instance):
        return instance.score.name

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Score, ScoreAdmin)
