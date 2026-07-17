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
        