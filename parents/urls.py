from django.urls import path

from . import views

urlpatterns = [
    path("", views.parents, name="parents"),
    path("student/<student_id>", views.parent_student, name="parent_student"),
    path("lessons/<lesson_id>", views.students_lesson_for_parents, name="students_lesson_for_parents"),
]
