from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from schedule.models import Teacher, TeacherInfo, Course, Student
from .forms import TeacherForm, CourseForm

def index(request):
    """Главная страница"""
    context = {
        'teachers_count': Teacher.objects.count(),
        'courses_count': Course.objects.count(),
        'students_count': Student.objects.count(),
    }
    return render(request, 'index.html', context)

def teacher_list(request):
    """Список всех преподавателей"""
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_add(request):
    """Добавление нового преподавателя"""
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            
            if form.cleaned_data.get('phone') or form.cleaned_data.get('bio'):
                TeacherInfo.objects.create(
                    teacher=teacher,
                    phone=form.cleaned_data.get('phone', ''),
                    bio=form.cleaned_data.get('bio', '')
                )
            
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    
    return render(request, 'teacher_add.html', {'form': form})

def courses(request):
    """Список всех курсов"""
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, pk):
    """Детальная информация о курсе"""
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def course_add(request):
    """Добавление нового курса"""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course.objects.create(
                title=form.cleaned_data['title'],
                teacher=form.cleaned_data['teacher']
            )
            return redirect('courses')
    else:
        form = CourseForm()
    
    return render(request, 'course_add.html', {'form': form})

def authors(request):
    """Список всех авторов (преподавателей)"""
    authors = Teacher.objects.all()
    
    for author in authors:
        student_ids = set()
        for course in author.courses.all():
            for student in course.students.all():
                student_ids.add(student.id)
        author.students_count = len(student_ids)
    
    return render(request, 'authors.html', {'authors': authors})


def author_details(request, pk):
    """Детальная информация об авторе (преподавателе)"""
    author = get_object_or_404(Teacher, pk=pk)
    author_courses = author.courses.all()
    
    return render(request, 'author_details.html', {
        'author': author,
        'courses': author_courses,
    })

def info(request):
    """Страница с ORM запросами"""
    teachers_with_multiple_courses = Teacher.objects.annotate(
        course_count=Count('courses')
    ).filter(course_count__gt=1)
    
    context = {
        'teachers_with_multiple_courses': teachers_with_multiple_courses,
    }
    return render(request, 'info.html', context)

def not_found(request):
    return render(request, '404.html')

def students(request):
    """Список всех студентов с их курсами"""
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})