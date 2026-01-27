from django.urls import path

from . import views

urlpatterns = [
    path("", views.teacher_page, name="teacher_page"),
    path("lessons", views.teacher_lessons, name="teacher_lessons"),
    path("lessons/<lesson_id>", views.teacher_specific_lesson, name="teacher_specific_lesson"),
    path("lessons/<lesson_id>/absence", views.absence, name="absence"),
    path("lessons/<lesson_id>/grade", views.grade, name="grade"),
    path("lessons/<lesson_id>/homework/<homework_id>", views.check_student_homework, name="check_student_homework")
]
