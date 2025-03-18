import requests

API_KEY = "b867a8218d174ff2916773813d472a3f"

BASE_URL = "https://api.currencyfreaks.com/latest"


def get_currency_rate(target_currency):
    """
    Отримує курс обміну валюти відносно USD.
    :param target_currency: Цільова валюта (наприклад, EUR)
    :return: Курс обміну
    """
    try:
        # Відправляємо GET-запит до API без параметра base
        response = requests.get(
            BASE_URL,
            params={
                "apikey": API_KEY,
            }
        )
        response.raise_for_status()  # Перевіряємо статус відповіді

        # Розбираємо JSON-відповідь
        data = response.json()

        # Отримуємо курс цільової валюти
        rate = data["rates"].get(target_currency)
        if rate:
            return float(rate)
        else:
            raise ValueError(f"Курс для валюти {target_currency} не знайдено.")
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
    except ValueError as e:
        print(f"Помилка: {e}")
