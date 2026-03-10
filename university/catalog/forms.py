from django import forms
from schedule.models import Teacher

class TeacherForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        label='Имя',
        help_text='(обязательно)',
        widget=forms.TextInput(attrs={
            'placeholder': 'ИМЯ',
        })
    )
    
    last_name = forms.CharField(
        max_length=100,
        label='Фамилия',
        help_text='(обязательно)',
        widget=forms.TextInput(attrs={
            'placeholder': 'ФАМИЛИЯ',
        })
    )
    
    email = forms.EmailField(
        required=False,
        label='Email',
        help_text='(необязательно)',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@mail.ru',
        })
    )
    
    phone = forms.CharField(
        required=False,
        max_length=20,
        label='Телефон',
        help_text='(необязательно)',
        widget=forms.TextInput(attrs={
            'placeholder': '+7 (123) 456-78-90',
        })
    )
    
    bio = forms.CharField(
        required=False,
        label='Биография',
        widget=forms.Textarea(attrs={
            'placeholder': 'ТЕКСТ',
            'rows': 4
        })
    )

class CourseForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Название курса',
        widget=forms.TextInput(attrs={
        })
    )
    
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        label='Преподаватель',
        empty_label='Выберите преподавателя',
        required=False
    )