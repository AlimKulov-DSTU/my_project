from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_name, validate_age, validate_experience_years, validate_start_date

class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100, 
        null=False,
        validators=[validate_name]
    )
    last_name = models.CharField(
        max_length=100, 
        null=False,
        validators=[validate_name]
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, validators=[validate_age])
    experience_years = models.IntegerField(null=True, blank=True, validators=[validate_experience_years])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        related_name='info',
        primary_key=True
    )
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )
    title = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True, blank=True, validators=[validate_start_date])
    
    def __str__(self):
        return self.title

class Student(models.Model):
    courses = models.ManyToManyField(Course, related_name='students')
    first_name = models.CharField(
        max_length=100,
        validators=[validate_name]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[validate_name]
    )
    age = models.IntegerField(null=True, blank=True, validators=[validate_age])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'