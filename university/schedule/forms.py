from django import forms

class TeacherForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        label='Имя',
        help_text='Введите имя преподавателя',
        widget=forms.TextInput(attrs={'placeholder': 'Например: Иван'})
    )
    
    last_name = forms.CharField(
        max_length=100,
        label='Фамилия',
        help_text='Введите фамилию преподавателя',
        widget=forms.TextInput(attrs={'placeholder': 'Например: Петров'})
    )
    
    email = forms.EmailField(
        required=False,
        label='Email',
        help_text='Введите email (необязательно)',
        widget=forms.EmailInput(attrs={'placeholder': 'ivan@university.ru'})
    )
    
    phone = forms.CharField(
        max_length=20,
        required=False,
        label='Телефон',
        help_text='Введите телефон (необязательно)',
        widget=forms.TextInput(attrs={'placeholder': '+7 (999) 123-45-67'})
    )
    
    bio = forms.CharField(
        required=False,
        label='Биография',
        help_text='Краткая информация о преподавателе',
        widget=forms.Textarea(attrs={
            'placeholder': 'Опыт работы, образование...',
            'rows': 4
        })
    )