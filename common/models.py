from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class SchoolClass(models.Model):
    start_year = models.IntegerField()
    letter = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.letter} class {self.start_year}"
    def __repr__(self):
        return f"{self.letter} class {self.start_year}"

class StudentClass(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    school_class = models.ForeignKey('SchoolClass', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} {self.school_class.letter} -> {self.school_class.start_year}"
    def __repr__(self):
        return f"{self.student.username} {self.school_class.letter} -> {self.school_class.start_year}"

class Contacts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_name = models.CharField(max_length=100)
    description = models.TextField()
    home_work = models.TextField()
    school_class = models.ForeignKey('SchoolClass', on_delete=models.CASCADE)

class Files(models.Model):
    file_path = models.FileField(upload_to='files/')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

class Grades(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='grades_as_student')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='grades_as_teacher')

class StudentHomework(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    text_data = models.TextField()
    grade = models.ForeignKey('Grades', on_delete=models.CASCADE)

class LessonVisits(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)