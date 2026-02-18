import datetime


def calc_period(date_in):
    if date_in.month >= 9:
        start_period = datetime.datetime(year=date_in.year, month=9, day=1)
        end_peroid = datetime.datetime(year=date_in.year+1, month=8, day=30)
    else:
        start_period = datetime.datetime(year=date_in.year-1, month=9, day=1)
        end_period = datetime.datetime(year=date_in.year, month=8, day=30)
        return start_period, end_period


def grade_update_handler(sender,*args, **kwargs):
    from common.models import Grades, StudentStatistics
    current_student = sender.student
    current_date = datetime.datetime.now()

    existing_student_average = StudentStatistics.objects.filter(student= current_student, end_period__gt=current_date)

    if existing_student_average is None:
        existing_student_average = StudentStatistics(student = current_student)
        start_period, end_period = calc_period(current_date)
        existing_student_average.start_period = start_period
        existing_student_average.end_period = end_period

    student_garde_objs = Grades.objects.filter(student = current_student, created_at__gt=existing_student_average.start_period)
    count_grades = len(student_garde_objs)
    all_grades = [one_grade.grade for one_grade in student_garde_objs]

    average = sum(all_grades)/count_grades
    existing_student_average.average = average
    existing_student_average.save()