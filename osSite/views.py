from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Grade, Teacher, VideoLesson, LessonSchedule
from .forms import GradeForm, LessonScheduleForm, UserCreationForm

from django.contrib.auth.decorators import login_required



def index(request):
    context = {"has_attribute":hasattr(request.user, 'teacher')}
    if request.user.is_authenticated:
        return render(request, 'osSite/index.html', context)
    else:
        return HttpResponseRedirect('login')



def grades(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'teacher'):
            return HttpResponseRedirect('/')
        else:
            grades = Grade.objects.filter(student=request.user)
            return render(request, 'osSite/grades.html', {'grades': grades})
    else:
        # return render(request, 'osSite/grades.html', {'error': 'Please, login to see your grades.'})
        # return render(request, 'osSite/login.html')
        return HttpResponseRedirect('login')


def video_lessons(request, video_id):
    current_video = get_object_or_404(VideoLesson, pk=video_id)
    next_video = VideoLesson.objects.filter(order__gt=current_video.order).first()
    prev_video = VideoLesson.objects.filter(order__lt=current_video.order).last()

    context = {
        'current_video': current_video,
        'next_video': next_video,
        'prev_video': prev_video,
        "has_attribute": hasattr(request.user, 'teacher')
    }

    return render(request, 'osSite/video_lessons.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'osSite/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'osSite/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

 

@login_required
def add_grade(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('home')
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.teacher = request.user.teacher
            grade.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'osSite/add_grade.html', {"has_attribute":hasattr(request.user, 'teacher'),
                                                     'form':form}
)



@login_required
def grade_list(request):
    if hasattr(request.user, 'teacher'):
        grades = Grade.objects.filter(teacher=request.user.teacher)
    else:
        grades = Grade.objects.filter(student__user=request.user)
    return render(request, 'osSite/grade_list.html', {'grades': grades})



@login_required
def schedule_list(request):
    if hasattr(request.user, 'teacher'):
        form = LessonScheduleForm()
        if request.method == 'POST':
            form = LessonScheduleForm(request.POST)
            if form.is_valid():
                lesson = form.save(commit=False)
                lesson.teacher = request.user
                lesson.save()
                return redirect('schedule')
        lessons = LessonSchedule.objects.filter(teacher=request.user).order_by('lesson_date')
        return render(request, 'osSite/schedule.html', {'form':form, 'lessons':lessons, 'has_attribute':True})
    else:
        lessons = LessonSchedule.objects.filter(student=request.user).order_by('lesson_date')
        return render(request, 'osSite/schedule.html', {'lessons': lessons, "has_attribute": False})



@login_required
def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(LessonSchedule, id=lesson_id)

    if request.user == lesson.teacher:
        lesson.delete()

    return redirect('schedule')