from django.test import TestCase, Client

from common.models import Lesson, SchoolClass, LessonVisits, StudentClass, Subject
from django.contrib.auth.models import User, Group

class TeacherTest(TestCase):

    def setUp(self):
        self.client = Client()

        teacher_group, _ = Group.objects.get_or_create(name="Teacher")
        self.teacher = User.objects.create_user("teacher1", password="1111")
        self.teacher.groups.add(teacher_group)
        self.client.login(username="teacher1", password="1111")

        self.subject = Subject.objects.create(name="Math")
        self.school_class = SchoolClass.objects.create(start_year=5, letter="d")

        self.student1 = User.objects.create_user("student1", password="1234")
        self.student2 = User.objects.create_user("student2", password="1234")
        StudentClass.objects.create(student=self.student1, school_class=self.school_class)
        StudentClass.objects.create(student=self.student2, school_class=self.school_class)

        self.lesson = Lesson.objects.create(
            subject=self.subject,
            teacher=self.teacher,
            lesson_date="2026-02-04",
            lesson_name="Lesson1",
            description="desc",
            home_work="hw",
            school_class=self.school_class
        )

    def test_teacher_page(self):
        response = self.client.get("/teacher/")
        self.assertEqual(response.status_code, 200)

    def test_teacher_lessons(self):
        response = self.client.get("/teacher/lessons")
        self.assertEqual(response.status_code, 200)

    def test_teacher_lessons_create(self):
        response = self.client.post("/teacher/lessons", {"subject": 1, "lesson_name": "Math_test", "lesson_date": "2026-09-01", "school_class": 1, "description": "test", "home_work": "test"})
        self.assertEqual(response.status_code, 302)
        created_lesson = Lesson.objects.get(lesson_name="Math_test")
        self.assertIsNotNone(created_lesson)
        self.assertEqual(created_lesson.school_class.pk, 1)

    def test_teacher_specific_lesson(self):
        response = self.client.get("/teacher/lessons/1")
        self.assertEqual(response.status_code, 200)

    def test_teacher_lessons_update(self):
        response = self.client.post("/teacher/lessons/1", {"subject": 1, "lesson_name": "Chemistry", "lesson_date": "2026-09-01", "school_class": 1, "description": "test", "home_work": "test"})
        self.assertEqual(response.status_code, 200)
        updated_lesson = Lesson.objects.get(pk=1)
        self.assertEqual(updated_lesson.lesson_name, "Chemistry")

    def test_set_absence(self):
        current_class = SchoolClass.objects.get(pk=1)
        current_students = current_class.studentclass_set.all()
        # set absent first student
        absent_student_ids = [current_students[0].student.id]
        response = self.client.post(f"/teacher/lessons/1/absence", {f"student-{absent_student_ids[0]}": absent_student_ids[0]})
        self.assertEqual(response.status_code, 302)
        lesson_visits = LessonVisits.objects.filter(lesson=1)
        self.assertEqual(lesson_visits.count(), 1)
        self.assertEqual(lesson_visits[0].student.pk, absent_student_ids[0])

        # set absent second student
        absent_student_ids = [current_students[0].student.id, current_students[1].student.id]
        formdata_dict = {f"student-{itm}": itm for itm in absent_student_ids}
        response = self.client.post(f"/teacher/lessons/1/absence", formdata_dict)
        self.assertEqual(response.status_code, 302)
        lesson_visits = LessonVisits.objects.filter(lesson=1).all()
        self.assertEqual(len(lesson_visits), 2)
        self.assertIsNotNone(LessonVisits.objects.filter(lesson=1, student=current_students[1].student).first())
        self.assertIsNotNone(LessonVisits.objects.filter(lesson=1, student=current_students[0].student).first())