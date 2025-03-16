from django.db import models
from users.models import User


class Advertisement(models.Model):
    CATEGORY_CHOICES = [
        ('sedan', 'Седан'),
        ('jeep', 'Позашляховик'),
        ('pickup', 'Пікап'),
        ('van', 'Фургон'),
        ('truck', 'Вантажівка'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="advertisements", verbose_name="Власник")
    car_name = models.CharField(max_length=255, verbose_name="Назва машини")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категорія")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Ціна")
    year_of_production = models.PositiveIntegerField(verbose_name="Рік випуску")
    mileage = models.PositiveIntegerField(verbose_name="Пробіг (км)")
    engine = models.CharField(max_length=100, verbose_name="Тип двигуна")
    location = models.CharField(max_length=255, verbose_name="Локація")
    owner_phone_number = models.CharField(max_length=15, verbose_name="Номер телефону власника")
    photo = models.ImageField(upload_to='car_photos/', verbose_name="Фото машини", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення оголошення")

    def __str__(self):
        return f"{self.car_name} - {self.price}$ ({self.created_at})"
