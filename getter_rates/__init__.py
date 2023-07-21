from datetime import date


def get_by_date(date_ref: date=date.today()):
    return {
        'date': date_ref,
        'brl': 1.0,
        'eur': 2.0,
        'jpy': 3.0,
    }
