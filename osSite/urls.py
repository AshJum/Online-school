from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='home'),
    path('videos/', views.video_lessons, name='video_lessons'),
    path('videos/<int:video_id>/', views.video_lessons, name='video_lessons'),
    path('grades/', views.grades, name='grades'),
    path('grades/add/', views.add_grade, name='add_grade'),
    path('grades/grade_list/', views.grade_list, name='grade_list'),
    path('schedule/', views.schedule_list, name='schedule'),
    path('schedule/delete/<int:lesson_id>/', views.delete_lesson, name='delete_lesson')
]