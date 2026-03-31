from django import forms
from schedule.models import Teacher, TeacherInfo, Course, Student
from datetime import date
import re

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'age', 'experience_years']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'age': 'Возраст',
            'experience_years': 'Опыт работы (лет)',
        }
        help_texts = {
            'first_name': 'Введите имя преподавателя (только буквы)',
            'last_name': 'Введите фамилию преподавателя (только буквы)',
            'email': 'Введите email (необязательно)',
            'age': 'Возраст преподавателя (18-100 лет)',
            'experience_years': 'Опыт работы в годах (0-50)',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Например: Иван'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Например: Петров'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ivan@university.ru'}),
            'age': forms.NumberInput(attrs={'placeholder': '30', 'min': 18, 'max': 100}),
            'experience_years': forms.NumberInput(attrs={'placeholder': '5', 'min': 0, 'max': 50}),
        }
    
    phone = forms.CharField(
        required=False,
        max_length=20,
        label='Телефон',
        help_text='Введите номер телефона (необязательно)',
        widget=forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'})
    )
    bio = forms.CharField(
        required=False,
        label='Биография',
        help_text='Краткая информация о преподавателе',
        widget=forms.Textarea(attrs={'placeholder': 'Опыт работы, образование...', 'rows': 4})
    )
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            first_name = first_name.strip()
            first_name = first_name.capitalize()
            first_name = ' '.join(first_name.split())
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            last_name = last_name.strip().capitalize()
            last_name = ' '.join(last_name.split())
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.strip()
            email = email.lower()
            if Teacher.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Преподаватель с таким email уже существует')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = re.sub(r'[^\d+\-]', '', phone)
            phone = phone.strip()
        return phone
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio:
            bio = bio.strip()
            bio = re.sub(r'\n\s*\n', '\n\n', bio)
        return bio
    
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        experience = cleaned_data.get('experience_years')
        
        if age and experience is not None:
            max_experience = age - 18
            if experience > max_experience:
                self.add_error('experience_years', f'Опыт работы ({experience} лет) не может превышать {max_experience} лет (возраст {age} минус 18)')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'teacher', 'start_date']
        labels = {
            'title': 'Название курса',
            'teacher': 'Преподаватель',
            'start_date': 'Дата начала',
        }
        help_texts = {
            'title': 'Введите название курса',
            'teacher': 'Выберите преподавателя (необязательно)',
            'start_date': 'Дата начала курса (не может быть в прошлом)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название'}),
            'teacher': forms.Select(attrs={'style': 'width: 100%; padding: 8px;'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            title = title.title()
            title = ' '.join(title.split())
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        start_date = cleaned_data.get('start_date')
        
        if start_date and not title:
            self.add_error('title', 'Если указана дата начала, название курса обязательно')
        
        return cleaned_data