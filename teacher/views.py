from django.http import HttpResponse
from django.shortcuts import render
from common.Forms import LessonForm
from common.models import Lesson
from common.tools import group_required


@group_required("Teacher")
def teacher_page(request):
    return HttpResponse("ok")

@group_required("Teacher")
def teacher_lessons(request):
    if request.method == "POST":
        create_lesson_form = LessonForm(request.POST)
        create_lesson_form.is_valid()
        lesson = Lesson(teacher=request.user, **create_lesson_form.cleaned_data)
        lesson.save()

    create_lesson_form = LessonForm()
    teacher_lessons_data = Lesson.objects.filter(teacher=request.user).all()
    return render(request, "teacher_lessons.html", context={"form":create_lesson_form,"teacher_lessons":teacher_lessons_data})


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
