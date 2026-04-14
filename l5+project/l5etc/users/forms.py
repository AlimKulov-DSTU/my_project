from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['username'].help_text = ''
        self.fields['email'].label = 'Email'
        self.fields['email'].help_text = ''
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = ''
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = ''
