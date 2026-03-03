from django.contrib import admin
from .models import Teacher, TeacherInfo, Course, Student

class TeacherInfoInline(admin.StackedInline):
    """Встраиваемая форма для TeacherInfo"""
    model = TeacherInfo
    can_delete = False

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Админка для преподавателей"""
    list_display = ('id', 'first_name', 'last_name', 'email', 'courses_count')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('courses',)
    inlines = [TeacherInfoInline]
    
    def courses_count(self, obj):
        return obj.courses.count()
    courses_count.short_description = 'Курсов'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка для курсов"""
    list_display = ('id', 'title', 'teacher', 'students_count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('teacher',)
    
    def students_count(self, obj):
        return obj.students.count() 
    students_count.short_description = 'Студентов'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Админка для студентов"""
    list_display = ('id', 'first_name', 'last_name', 'courses_count')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    filter_horizontal = ('courses',)
    
    def courses_count(self, obj):
        return obj.courses.count()
    courses_count.short_description = 'Курсов'