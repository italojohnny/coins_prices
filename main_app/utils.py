from getter_rates import get_by_date
from datetime import date, timedelta
from coins_prices.config import Config

config = Config()
MAX_DATA_RANGE = config.main_app.date_range


class InvalidDateRange(Exception):
    def __str__(self):
        return 'Date range is invalid!'


def get_rates(coin_name, date1=None, date2=None):
    result = list()
    date_range = get_date_range(date1, date2)
    for d in date_range:
        result.append(get_rate(coin_name, d))
    return result


def get_date_range(date1, date2):
    '''
    obtem intervalo de datas respeitando regra de intervalo maximo entre elas
    '''
    diff = 1 + abs(date1 - date2).days
    if diff > MAX_DATA_RANGE:
        raise InvalidDateRange

    current, last = min(date1, date2), max(date1, date2)

    dates = list()
    while current <= last:
        dates.append(current)
        current += timedelta(days=1)
    return dates


def get_rate(d, coin_name):
    result = get_by_date(d)
    return {
        'date': result.get('date'),
        'value': result.get(coin_name),
    }
