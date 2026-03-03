from django.shortcuts import render
from .models import Teacher

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Teacher, TeacherInfo, Course, Student

# Create your views here.

def index(request):
    """Главная страница приложения"""
    teachers_count = Teacher.objects.count()
    courses_count = Course.objects.count()
    students_count = Student.objects.count()
    
    context = {
        'teachers_count': teachers_count,
        'courses_count': courses_count,
        'students_count': students_count,
    }
    return render(request, 'schedule/index.html', context)

def teacher_list(request):
    """Список всех преподавателей"""
    teachers = Teacher.objects.all()
    return render(request, 'schedule/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    """Детальная информация о преподавателе"""
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'schedule/teacher_detail.html', {'teacher': teacher})