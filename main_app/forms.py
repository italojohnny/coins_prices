from django import forms
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
