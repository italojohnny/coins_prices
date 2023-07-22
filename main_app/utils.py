from getter_rates import get_by_date
from datetime import date


def get_rates():
    return [
        get_by_date(date(2023, 7, 17)),
        get_by_date(date(2023, 7, 18)),
        get_by_date(date(2023, 7, 19)),
        get_by_date(date(2023, 7, 20)),
        get_by_date(date(2023, 7, 21)),
    ]
