from django.shortcuts import render, redirect
from .utils import get_cached_currency_rate
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.db.models import F, FloatField
from django.db.models.functions import Round
from .models import Advertisement
from .forms import AdvertisementForm


def home(request):
    rate = round(get_cached_currency_rate("UAH"), 2)
    unique_users_count = Advertisement.objects.values("owner").distinct().count()
    if unique_users_count == 1 or unique_users_count % 10 == 1:
        users_text = f"{unique_users_count} користувач вже розмістив свої оголошення"
    elif unique_users_count in [2, 3, 4] and unique_users_count not in [12, 13, 14]:
        users_text = f"{unique_users_count} користувачі вже розмістили свої оголошення"
    else:
        users_text = f"{unique_users_count} користувачів вже розмістили свої оголошення"

    return render(request, 'main/index.html', {'rate': rate, 'users_text': users_text})


def about(request):
    rate = round(get_cached_currency_rate("UAH"), 2)
    return render(request, 'main/about.html', {'rate': rate})


def advertisements(request):
    rate = Decimal(str(round(get_cached_currency_rate("UAH"), 2)))
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.get('category')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    min_miles = request.GET.get('min_miles')
    max_miles = request.GET.get('max_miles')
    location = request.GET.get('location')

    advertisements = Advertisement.objects.annotate(
        price_uah=Round(F("price") * rate, 0)
    )

    if min_price:
        advertisements = advertisements.filter(price__gte=min_price)
    if max_price:
        advertisements = advertisements.filter(price__lte=max_price)
    if category:
        advertisements = advertisements.filter(category=category)
    if min_year:
        advertisements = advertisements.filter(year_of_production__gte=min_year)
    if max_year:
        advertisements = advertisements.filter(year_of_production__lte=max_year)
    if min_miles:
        advertisements = advertisements.filter(mileage__gte=min_miles)
    if max_miles:
        advertisements = advertisements.filter(mileage__lte=max_miles)
    if location:
        advertisements = advertisements.filter(location=location)

    count = advertisements.count()
    if count % 10 == 1 and count % 100 != 11:
        count_text = f"Знайдено {count} оголошення"
    elif count % 10 in [2, 3, 4] and count % 100 not in [12, 13, 14]:
        count_text = f"Знайдено {count} оголошення"
    else:
        count_text = f"Знайдено {count} оголошень"

    context = {
        'advertisements': advertisements,
        'rate': rate,
        'min_price': min_price,
        'max_price': max_price,
        'category': category,
        'min_year': min_year,
        'max_year': max_year,
        'min_miles': min_miles,
        'max_miles': max_miles,
        'location': location,
        'count_text': count_text
    }

    return render(request, 'main/advertisements.html', context)


def advertisement_detail(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id)
    rate = Decimal(str(round(get_cached_currency_rate("UAH"), 2)))
    ad.price_uah = round(ad.price * rate, 0)

    context = {
        'advertisement': ad,
        'rate': rate,
    }
    return render(request, 'main/advertisement_detail.html', context)


def create_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.owner = request.user  # Встановлюємо власника як поточного користувача
            advertisement.save()
            return redirect('main:home')
    else:
        form = AdvertisementForm()
    return render(request, 'main/create_advertisement.html', {'form': form})


def contacts(request):
    rate = round(get_cached_currency_rate("UAH"), 2)
    return render(request, 'main/contacts.html', {'rate': rate})
