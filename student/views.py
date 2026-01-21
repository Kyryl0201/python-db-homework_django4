from django.shortcuts import render

# Create your views here.
def student_page(request):
    return "ok"

def student_lessons(request):
    return "ok"

def student_specific_lesson(request, lesson_id):
    return f"ok {lesson_id}"

def submit_homework(request, lesson_id):
    return f"ok {lesson_id}"
