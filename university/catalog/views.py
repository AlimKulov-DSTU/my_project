from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from schedule.models import Teacher, Course, Student

def index(request):
    """Главная страница"""
    context = {
        'teachers_count': Teacher.objects.count(),
        'courses_count': Course.objects.count(),
        'students_count': Student.objects.count(),
    }
    return render(request, 'index.html', context)

def courses(request):
    """Список всех курсов"""
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, pk):
    """Детальная информация о курсе"""
    course = get_object_or_404(Course, pk=pk)
    author = course.teacher
    
    return render(request, 'course_detail.html', {
        'course': course,
        'author': author,
    })

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
    
    # 1. Преподаватели, у которых больше 1 курса
    teachers_with_multiple_courses = Teacher.objects.annotate(
        course_count=Count('courses')
    ).filter(course_count__gt=1)
    
    # 2. Студенты без курсов
    students_without_courses = Student.objects.filter(courses__isnull=True)
    
    # 3. Преподаватели без профиля (TeacherInfo)
    teachers_without_profile = Teacher.objects.filter(info__isnull=True)
    
    # 4. статистика
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()
    total_students = Student.objects.count()
    
    context = {
        'teachers_with_multiple_courses': teachers_with_multiple_courses,
        'students_without_courses': students_without_courses,
        'teachers_without_profile': teachers_without_profile,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
        'total_students': total_students,
    }
    return render(request, 'orm_queries.html', context)

def not_found(request):
    """Страница 404"""
    return render(request, '404.html')

def students(request):
    """Список всех студентов с их курсами"""
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})