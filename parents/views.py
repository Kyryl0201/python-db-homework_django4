from django.shortcuts import render

# Create your views here.
def parents(request):
    return "ok"

def parent_student(request, student_id):
    return f"ok {student_id}"

def students_lesson_for_parents(request, lesson_id):
    return f"ok {lesson_id}"