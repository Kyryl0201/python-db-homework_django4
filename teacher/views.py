from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.Forms import LessonForm
from common.models import Lesson, StudentClass, LessonVisits
from common.tools import group_required


@group_required("Teacher")
def teacher_page(request):
    return HttpResponse("ok")

@group_required("Teacher")
def teacher_lessons(request):
    if request.method == "POST":
        form = LessonForm(request.POST)

        if form.is_valid():
            Lesson.objects.create(
                teacher=request.user,
                **form.cleaned_data
            )
            return redirect("teacher_lessons")
    else:
        form = LessonForm()

    teacher_lessons_data = Lesson.objects.filter(teacher=request.user)

    return render(request, "teacher_lessons.html", {
        "form": form,
        "teacher_lessons": teacher_lessons_data,
    })


@group_required("Teacher")
def teacher_specific_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    current_class = lesson.school_class
    students_in_class = [itm.student for itm in StudentClass.objects.filter(school_class=current_class).all()]

    absence_students_ids = [itm.student.id for itm in LessonVisits.objects.filter(lesson=lesson).all()]

    for student in students_in_class:
        student.is_absent = "checked" if student.id in absence_students_ids else ""

    if request.method == "POST":
        update_lesson_form = LessonForm(request.POST, instance=lesson)
        update_lesson_form.is_valid()
        update_lesson_form.save()
    else:
        update_lesson_form = LessonForm(instance=lesson)
        
    return render(request, "one_lesson.html", context={"form":update_lesson_form, "lesson":lesson, "class_students":students_in_class})


@group_required("Teacher")
def absence(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("student"):
                student = User.objects.get(id=int(value))
                if not LessonVisits.objects.filter(student=student, lesson=lesson).exists():
                    lesson_absence_student_form = LessonVisits.objects.create(student=student, lesson=lesson)
                    lesson_absence_student_form.save()

    return redirect("teacher_specific_lesson", lesson_id=lesson_id)


@group_required("Teacher")
def grade(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")


@group_required("Teacher")
def check_student_homework(request, lesson_id, homework_id):
    return HttpResponse(f"ok {lesson_id} here is {homework_id}")
