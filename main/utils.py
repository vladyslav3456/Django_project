from django.core.cache import cache
from .rate import get_currency_rate


def get_cached_currency_rate(target_currency):
    cache_key = f"currency_rate_{target_currency}"
    rate = cache.get(cache_key)

    if rate is None:
        rate = get_currency_rate(target_currency)
        cache.set(cache_key, rate, 24 * 60 * 60)  # Кешуємо на 24 години

    return rate
