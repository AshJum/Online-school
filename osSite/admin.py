from django.contrib import admin
from .models import Grade, Teacher, VideoLesson, LessonSchedule

admin.site.register(VideoLesson)
admin.site.register(Grade)
admin.site.register(Teacher)
admin.site.register(LessonSchedule)


#username - teacherTest   password-test.1234     ---     user type - teacher
#username - userTesting-4   password-Test.1234     ---     user. type - student