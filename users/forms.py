from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
import re


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True, min_value=18)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'age']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not re.match(r'^\w+$', username):
            raise ValidationError("Логін не може містити інших символів, окрім літер, цифр та _ (підкреслення).")
        if not any(char.isalpha() for char in username):
            raise ValidationError("Логін не може складатись лише з цифр.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Користувач з таким логіном вже існує.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Цей email вже зареєстрований.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name.isalpha():
            raise ValidationError("Ім'я має містити лише літери.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name.isalpha():
            raise ValidationError("Прізвище має містити лише літери.")
        return last_name

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Пароль має містити щонайменше 8 символів.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Пароль повинен містити хоча б одну цифру.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Пароль повинен містити хоча б одну літеру.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if len(password2) < 8:
            raise ValidationError("Пароль має містити щонайменше 8 символів.")
        if not any(char.isdigit() for char in password2):
            raise ValidationError("Пароль повинен містити хоча б одну цифру.")
        if not any(char.isalpha() for char in password2):
            raise ValidationError("Пароль повинен містити хоча б одну літеру.")
        return password2

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not re.match(r'^\+?\d{10,15}$', phone_number):
            raise ValidationError("Введіть номер телефон у форматі +380XXXXXXXXX.")
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Цей номер телефону вже зареєстрований.")
        return phone_number

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise ValidationError("Вам має бути щонайменше 18 років для реєстрації.")
        if age > 120:
            raise ValidationError("Вам не може бути більше 120 років.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')
        if password != confirm_password:
            self.add_error('password1', "Паролі не збігаються.")
            self.add_error('password2', 'Паролі не збігаються.')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'age']
