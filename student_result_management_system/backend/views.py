from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from .serializers import ResultSerializer
from .serializers import ScoreSerializer
from .models import Student
from .models import Course
from .models import Result
from .models import Score
import json
from django.core import serializers
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ResultView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    # model = Result
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

    # name = request.data.get('name')

    # def list(self, request):
    #     queryset = Result.objects.all()
    #     serializer = ResultSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     pk = request.data.get('student_id')
    #     queryset = Result.objects.all()
    #     result = get_object_or_404(queryset, pk=pk)
    #     serializer = ResultSerializer(result)
    #     return Response(serializer.data)

    # def post(self,request,*args, **kwargs):
    #     body = json.loads(request.body.decode("utf-8"))
    #     result = Result.objects.create(student=body['student_id'], course=body['course_id'], score=body['score_id'])
    #     data = json.loads(serializers.serialize('json',[result]))
    #     return JsonResponse({'success':data})

class ScoreView(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
