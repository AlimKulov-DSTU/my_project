import logging

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User

logger = logging.getLogger(__name__)


class AvatarImageField(forms.ImageField):
    def to_python(self, data):
        try:
            return super().to_python(data)
        except ValidationError:
            logger.error('Invalid avatar upload', exc_info=True)
            raise


class UserUniqueFieldsMixin:
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        queryset = User.objects.filter(email=email)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if not phone:
            return phone
        queryset = User.objects.filter(phone=phone)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Пользователь с таким телефоном уже существует.')
        return phone


class RegisterForm(UserUniqueFieldsMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone')
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'phone': 'Телефон',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите телефон'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['phone'].required = False
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = ''
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = ''


class ProfileForm(UserUniqueFieldsMixin, forms.ModelForm):
    avatar = AvatarImageField(label='Аватар', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'avatar')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Телефон',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите телефон'}),
        }
