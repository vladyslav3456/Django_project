from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # Визначаємо, які поля відображати в списку користувачів
    list_display = ('username', 'password', 'phone_number', 'age', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')

    # Визначаємо, які поля відображати у формі редагування
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'age')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Додаємо поля для пошуку по адмінці
    search_fields = ('username', 'email', 'phone_number')
    # Додаємо поля для фільтрації
    ordering = ('username',)


# Реєструємо модель з кастомним адмінським класом
admin.site.register(User, CustomUserAdmin)
