import requests
from pydantic import BaseModel, Field
from dateutil import parser
from datetime import date


class Currencies(BaseModel):
    jpy: float = Field(..., alias='JPY')
    eur: float = Field(..., alias='EUR')
    brl: float = Field(..., alias='BRL')


class VatResponse(BaseModel):
    base: str
    date: date
    rates: Currencies


def get_by_date(date_ref: date=date.today()):
    try:
        date_ref = parser.parse(str(date_ref)).date()

    except parser._parser.ParserError:
        pass

    endpoint = f'https://api.vatcomply.com/rates?base=USD&date={date_ref}'
    response = requests.get(endpoint)
    response.raise_for_status()
    vat = VatResponse(**response.json())

    return {
        'date': vat.date,
        'brl': vat.rates.brl,
        'eur': vat.rates.eur,
        'jpy': vat.rates.jpy,
    }
