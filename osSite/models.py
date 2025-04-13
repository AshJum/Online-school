from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} ({self.subject})"


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades', verbose_name="Ուսանող")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='grades', null=True)
    subject = models.CharField(max_length=100, verbose_name="Առարկա")
    score = models.PositiveIntegerField(verbose_name="Գնահատական")
    date = models.DateField(auto_now_add=True, verbose_name="Ամսաթիվ")

    def __str__(self):
        return f"{self.student.username} - {self.subject} - {self.score}"



class VideoLesson(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.title



class LessonSchedule(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_as_teacher')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons_as_student', verbose_name="Ուսանող")
    lesson_date = models.DateTimeField(verbose_name="դասաժամ")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lesson on {self.lesson_date} with {self.student.username}"

