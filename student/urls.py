from django.urls import path

from . import views

urlpatterns = [
    path("", views.student_page, name="student_page"),
    path("lessons", views.student_lessons, name="student_lessons"),
    path("lessons/<lesson_id>", views.student_specific_lesson, name="student_specific_lesson"),
    path("lessons/<lesson_id>/submit_homework", views.submit_homework, name="submit_homework"),
]