from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.models import Course,Lesson,SupportingDoc,Quiz
from course.serializers import (
    CourseSerializer,
    LessonSerializer,
    SupportingDocSerializer,
    QuizSerializer
)
from course.permissions import IsInstructorOnly
from rest_framework.permissions import IsAuthenticated,AllowAny


class CourseListView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        try:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CourseCreateView(APIView):
    permission_classes = [IsInstructorOnly]
    def post(self,request):
        try:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)