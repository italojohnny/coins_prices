from getter_rates import get_by_date
from datetime import date, timedelta
from coins_prices.config import Config
from getter_rates import Currencies
from .models import RateModel


config = Config()
COINS_ALLOWED = Currencies.__fields__.keys()
MAX_DATA_RANGE = config.main_app.date_range
DATE_FORMAT = '%Y-%m-%d'


class InvalidDateRange(Exception):
    def __str__(self):
        return 'Date range is invalid!'


def remove_duplicate(rates):
    '''
    Remove cotacoes repetidas
    '''
    cleaned_rates = list()
    historic = list()
    for rate in rates:
        if rate['date'] not in historic:
            historic.append(rate['date'])
            cleaned_rates.append(rate)

    return cleaned_rates


def get_rates(coin_name, date1=None, date2=None):
    '''
    obtem cotacoes de uma moeda em um determinado intervalo de datas
    '''
    today = date.today()
    date1 = date1 or date2 or today
    date2 = date2 or date1 or today

    result = list()
    date_range = get_date_range(date1, date2)
    for d in date_range:
        result.append(get_rate(coin_name, d))

    return remove_duplicate(result)


def get_date_range(date1, date2):
    '''
    obtem intervalo de datas respeitando regra de intervalo maximo entre elas
    '''
    diff = 1 + abs(date1 - date2).days
    if diff > MAX_DATA_RANGE:
        raise InvalidDateRange

    current, last = min(date1, date2), max(date1, date2)

    date_range = list()
    while current <= last:
        date_range.append(current)
        current += timedelta(days=1)
    return date_range


def get_rate(coin_name, d):
    '''
    obtem cotacao de uma moeda em uma determinada data
    '''
    try:
        result = get_rate_from_database(coin_name, d)
        if not result:
            result = get_by_date(d)
            set_rate_in_database(result)

    except Exception:
        result = dict()

    return {
        'date': result.get('date'),
        'value': result.get(coin_name),
    }


def get_rate_from_database(coin_name, d):
    '''
    obtem cotacao de uma moeda em uma determinada data
    '''
    result = RateModel.objects.filter(date=d).first()
    if result:
        return result.__dict__
    return None


def set_rate_in_database(rate):
    '''
    salva cotacao no banco cotacao
    '''
    defaults = rate.copy()
    defaults.pop('date', None)
    return RateModel.objects.update_or_create(
        date=rate.get('date'),
        defaults=defaults,
    )
