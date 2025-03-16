from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, verbose_name="Номер телефону")
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(120)],
        verbose_name="Вік",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
