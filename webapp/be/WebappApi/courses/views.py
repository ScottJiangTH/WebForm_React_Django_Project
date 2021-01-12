from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from courses.models import Course
from courses.models import Outcome
from courses.models import GraduateAttribute
from courses.models import ContentCategory
from courses.models import Section
from courses.models import LabExperience
from courses.models import FinalGrade
from courses.models import LetterGrade

from courses.serializers import CourseSerializer
from courses.serializers import OutcomeSerializer
from courses.serializers import GraduateAttributeSerializer
from courses.serializers import ContentCategorySerializer
from courses.serializers import SectionSerializer
from courses.serializers import LabExperienceSerializer
from courses.serializers import FinalGradeSerializer
from courses.serializers import LetterGradeSerializer

from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        
        courseNumber = request.query_params.get('courseNumber', None)
        if courseNumber is not None:
            courses = courses.filter(title__icontains=courseNumber)
        
        courses_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Echo.objects.all().delete()
        return JsonResponse({'message': '{} Echos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try: 
        echo = Echo.objects.get(pk=pk) 
    except Echo.DoesNotExist: 
        return JsonResponse({'message': 'The echo does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        echo_serializer = EchoSerializer(echo) 
        return JsonResponse(echo_serializer.data) 
 
    elif request.method == 'PUT': 
        echo_data = JSONParser().parse(request) 
        echo_serializer = EchoSerializer(echo, data=echo_data) 
        if echo_serializer.is_valid(): 
            echo_serializer.save() 
            return JsonResponse(echo_serializer.data) 
        return JsonResponse(echo_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        echo.delete() 
        return JsonResponse({'message': 'Echo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        