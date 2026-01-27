from django.http import HttpResponse
from django.shortcuts import render
from common.tools import group_required


@group_required("Teacher")
def teacher_page(request):
    return HttpResponse("ok")


@group_required("Teacher")
def teacher_lessons(request):
    return HttpResponse("ok")


@group_required("Teacher")
def teacher_specific_lesson(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")


@group_required("Teacher")
def absence(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")


@group_required("Teacher")
def grade(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")


@group_required("Teacher")
def check_student_homework(request, lesson_id, homework_id):
    return HttpResponse(f"ok {lesson_id} here is {homework_id}")
