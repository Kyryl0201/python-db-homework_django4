from django.shortcuts import render

# Create your views here.
def teacher_page(request):
    return "ok"

def teacher_lessons(request):
    return "ok"

def specific_lesson(request, lesson_id):
    return f"ok {lesson_id}"

def absence(request, lesson_id):
    return f"ok {lesson_id}"

def grade(request, lesson_id):
    return f"ok {lesson_id}"

def check_student_homework(request, lesson_id, homework_id):
    return f"ok {lesson_id} here is {homework_id}"