# catalog/views.py
from django.shortcuts import render

from .temp_data import AUTHORS, COURSES


def index(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html', {'courses': COURSES})


def course_detail(request, pk):
    course = None
    author = None
    
    for c in COURSES:
        if c['id'] == pk:
            course = c
            break
    
    if course:
        for a in AUTHORS:
            if a['id'] == course['author_id']:
                author = a
                break
    
    return render(request, 'course_detail.html', {
        'course': course,
        'author': author,
    })


def authors(request):
    return render(request, 'authors.html', {'authors': AUTHORS})


def author_details(request, pk):
    author = None
    author_courses = []
    
    for a in AUTHORS:
        if a['id'] == pk:
            author = a
            break
    
    if author:
        for c in COURSES:
            if c['author_id'] == author['id']:
                author_courses.append(c)
    
    return render(request, 'author_details.html', {
        'author': author,
        'courses': author_courses,
    })


def info(request):
    return render(request, 'info.html')

def not_found(request):
    return render(request, '404.html')