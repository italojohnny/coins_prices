from getter_rates import get_by_date
from datetime import date
from coins_prices.config import Config

config = Config()
MAX_DATA_RANGE = config.main_app.date_range

def get_rates(coin_name):
    return [
        get_rate(date(2023, 7, 17), coin_name),
        get_rate(date(2023, 7, 18), coin_name),
        get_rate(date(2023, 7, 19), coin_name),
        get_rate(date(2023, 7, 20), coin_name),
        get_rate(date(2023, 7, 21), coin_name),
    ]


def get_rate(d, coin_name):
    result = get_by_date(d)
    return {
        'date': result.get('date'),
        'value': result.get(coin_name),
    }
