from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("car_name", "price", "owner", "created_at")
    search_fields = ("car_name", "owner__username", "location")
