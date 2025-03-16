from django import forms
from django.core.exceptions import ValidationError
from .models import Advertisement
import re


class AdvertisementForm(forms.ModelForm):
    owner = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Advertisement
        fields = ['car_name', 'category', 'price', 'year_of_production', 'mileage',
                  'engine', 'location', 'owner_phone_number', 'photo']
        widgets = {
            'category': forms.Select(choices=Advertisement.CATEGORY_CHOICES),
        }

    def clean_car_name(self):
        car_name = self.cleaned_data.get("car_name")
        if not any(char.isalpha() for char in car_name):
            raise ValidationError("Модель автомобіля повинна містити хоча б одну літеру.")
        return car_name

    def clean_year_of_production(self):
        year_of_production = self.cleaned_data.get("year_of_production")
        if year_of_production < 1990:
            raise ValidationError("Рік випуску автомобіля не може бути меншим за 1990.")
        if year_of_production > 2025:
            raise ValidationError("Рік випуску автомобіля не може бути більшим за 2025.")
        return year_of_production

    def clean_engine(self):
        engine = self.cleaned_data.get("engine")
        if not any(char.isdigit() for char in engine):
            raise ValidationError("Тип двигуна повинен містити хоча б одну цифру.")
        if not any(char.isalpha() for char in engine):
            raise ValidationError("Тип двигуна повинен містити хоча б одну літеру.")
        return engine

    def clean_location(self):
        location = self.cleaned_data.get("location")
        if not any(char.isalpha() for char in location):
            raise ValidationError("Локація розташування автомобіля повинна містити хоча б одну літеру.")
        return location

    def clean_owner(self):
        owner = self.cleaned_data.get("owner")
        if not any(char.isalpha() for char in owner):
            raise ValidationError("Ініціали продавця повинні містити хоча б одну літеру.")
        return owner

    def clean_owner_phone_number(self):
        owner_phone_number = self.cleaned_data.get("owner_phone_number")
        if not re.match(r'^\+?\d{10,15}$', owner_phone_number):
            raise ValidationError("Введіть номер телефон у форматі +380XXXXXXXXX.")
        return owner_phone_number
