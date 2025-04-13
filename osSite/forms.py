from django import forms
from .models import Grade, LessonSchedule, User
from django.contrib.auth.forms import UserCreationForm

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']


class LessonScheduleForm(forms.ModelForm):
    class Meta:
        model = LessonSchedule
        fields = ['student', 'lesson_date']
        widgets = {
            'lesson_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Մուտքանուն'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Գաղտնաբառ'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Կրկնել գաղտնաբառը'}),
        }
