import requests
from datetime import date



def get_by_date(date_ref: date=date.today()):
    if not date_ref:
        date_ref = date.today()

    endpoint = f'https://api.vatcomply.com/rates?base=USD&date={date_ref}'
    response = requests.get(endpoint)
    response.raise_for_status()
    raw = response.json()

    return {
        'date': raw['date'],
        'brl': raw['rates']['BRL'],
        'eur': raw['rates']['EUR'],
        'jpy': raw['rates']['JPY'],
    }
