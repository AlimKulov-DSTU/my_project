from django.shortcuts import render, redirect
from .models import Teacher, TeacherInfo, Course
from .forms import TeacherForm

def teacher_list(request):
    """Список всех преподавателей"""
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    """Добавление нового преподавателя"""
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            # Создаем преподавателя
            teacher = Teacher.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            
            # Создаем дополнительную информацию
            if form.cleaned_data['phone'] or form.cleaned_data['bio']:
                TeacherInfo.objects.create(
                    teacher=teacher,
                    phone=form.cleaned_data['phone'],
                    bio=form.cleaned_data['bio']
                )
            
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    
    return render(request, 'teacher_form.html', {'form': form})

def course_list(request):
    """Список всех курсов"""
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_create(request):
    """Добавление курса (заглушка)"""
    return render(request, 'course_form.html')