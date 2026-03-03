import django
from django.db import models
from django.db import migrations

class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=True, blank=True)  

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
    title = models.CharField(
        max_length=100,
        null=False
    )
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    courses = models.ManyToManyField(
        Course, 
        related_name='students'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'