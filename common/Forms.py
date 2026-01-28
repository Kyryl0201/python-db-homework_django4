from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Form, CharField, DateInput

from common.models import Lesson


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LoginForm(Form):
    login = CharField(max_length=200)
    password = CharField(max_length=200)

class DateInput_custom(DateInput):
    input_type = 'date'

class LessonForm(ModelForm):

    class Meta:
        model = Lesson
        exclude = ["teacher"]
        widgets = {
            'lesson_date': DateInput_custom(attrs={'class': 'form-control'}),
        }