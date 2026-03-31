import re
from django.core.exceptions import ValidationError
from datetime import date

def validate_name(value):
    """Валидатор: имя/фамилия должны содержать только буквы, дефис и пробел"""
    if value:
        #Убираем пробелы в начале и конце для проверки
        cleaned = value.strip()
        #Разрешаем буквы (русские и английские), дефис и пробел
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\-\s]+$', cleaned):
            raise ValidationError('Имя/фамилия должны содержать только буквы, дефис или пробел')
        #Проверяем, что не состоит только из пробелов
        if len(cleaned.strip()) == 0:
            raise ValidationError('Имя/фамилия не могут быть пустыми')
        #Первая буква должна быть буквой
        if not cleaned[0].isalpha():
            raise ValidationError('Имя/фамилия должны начинаться с буквы')

def validate_age(value):
    """Валидатор: возраст от 18 до 100 лет"""
    if value is not None:
        if value < 18:
            raise ValidationError('Возраст не может быть меньше 18 лет')
        if value > 100:
            raise ValidationError('Возраст не может превышать 100 лет')

def validate_experience_years(value):
    """Валидатор: опыт работы от 0 до 50 лет"""
    if value is not None:
        if value < 0:
            raise ValidationError('Опыт работы не может быть отрицательным')
        if value > 50:
            raise ValidationError('Опыт работы не может превышать 50 лет')

def validate_start_date(value):
    """Валидатор: дата начала курса не может быть в прошлом"""
    if value and value < date.today():
        raise ValidationError('Дата начала курса не может быть в прошлом')

def validate_phone(value):
    """Валидатор: телефон должен содержать только цифры, + и -"""
    if value:
        if not re.match(r'^[\d+\-\s]+$', value):
            raise ValidationError('Телефон должен содержать только цифры, + и -')