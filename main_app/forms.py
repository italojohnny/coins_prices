from django import forms
from main_app import utils
from datetime import date


class FormIndex(forms.Form):
    begin = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'})
    )
    end = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker'})
    )
    coin = forms.ChoiceField(
        choices=(
            ('brl', 'Real'),
            ('eur', 'Euro'),
            ('jpy', 'Iene'),
        )
    )

    def is_future_date(self, d):
        if d > date.today():
            return True

    def is_date_reversed(self, d1, d2):
        if d1 > d2:
            return True

    def is_range_invalid(self, d1, d2):
        diff = abs(d1 - d2).days + 1
        if diff > utils.MAX_DATA_RANGE:
            return True

    def is_coin_invalid(self, coin):
        if coin not in utils.COINS_ALLOWED:
            return True
