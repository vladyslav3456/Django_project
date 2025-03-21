# Generated by Django 4.2.18 on 2025-03-14 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=255, verbose_name='Назва машини')),
                ('category', models.CharField(choices=[('sedan', 'Седан'), ('jeep', 'Позашляховик'), ('pickup', 'Пікап'), ('van', 'Фургон'), ('truck', 'Вантажівка')], max_length=20, verbose_name='Категорія')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('year_of_production', models.PositiveIntegerField(verbose_name='Рік випуску')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробіг (км)')),
                ('engine', models.CharField(max_length=100, verbose_name='Тип двигуна')),
                ('location', models.CharField(max_length=255, verbose_name='Локація')),
                ('owner_phone_number', models.CharField(max_length=15, verbose_name='Номер телефону власника')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='car_photos/', verbose_name='Фото машини')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення оголошення')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='Власник')),
            ],
        ),
    ]
