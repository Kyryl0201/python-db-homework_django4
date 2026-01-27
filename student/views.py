from django.http import HttpResponse
from django.shortcuts import render
from common.tools import group_required


@group_required("Student")
def student_page(request):
    return HttpResponse("ok")


@group_required("Student")
def student_lessons(request):
    return HttpResponse("ok")


@group_required("Student")
def student_specific_lesson(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")


@group_required("Student")
def submit_homework(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")

