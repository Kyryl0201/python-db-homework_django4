from django.http import HttpResponse
from django.shortcuts import render
from common.tools import group_required


@group_required("Parents")
def parents(request):
    return HttpResponse("ok")


@group_required("Parents")
def parent_student(request, student_id):
    return HttpResponse(f"ok {student_id}")


@group_required("Parents")
def students_lesson_for_parents(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")
