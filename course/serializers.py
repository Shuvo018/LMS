from rest_framework import serializers
from course.models import Course,Lesson,SupportingDoc,Quiz

class SupportingDocSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    class Meta:
        model = SupportingDoc
        fields = ('lesson','title','file')


class QuizSerializer(serializers.ModelSerializer):
     class Meta:
        model = Quiz
        fields = ('id','lesson','question','answer_choices','correct_choice')


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.FileField(required=False)
    supporting_docs = SupportingDocSerializer(many=True,read_only=True)
    quizzes = QuizSerializer(many=True,read_only=True)
    class Meta:
        model = Lesson
        fields = ('id','course','title','content','video','order','supporting_docs',"quizzes")


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ('id','title','description','lessons')


