from django.contrib import admin

from .models import Course, Lesson, SupportingDoc, Quiz

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(SupportingDoc)
admin.site.register(Quiz)