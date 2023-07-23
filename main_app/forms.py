from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        cleaned_data = super().clean()
        begin = cleaned_data.get('begin')
        end = cleaned_data.get('end')
        coin = cleaned_data.get('coin')
        exceptions = list()

        if self.is_future_date(begin):
            exceptions.append(
                ValidationError(
                    'Data inicial invalida. '
                    'Use apenas datas no passado ou presente.'
                )
            )

        if self.is_future_date(end):
            exceptions.append(
                ValidationError(
                    'Data final invalida. '
                    'Use apenas datas no passado ou presente.'
                )
            )

        if self.is_date_reversed(begin, end):
            exceptions.append(
                ValidationError(
                    'Data inicial não pode ser maior que a data final.'
                )
            )
        if self.is_range_invalid(begin, end):
            exceptions.append(
                ValidationError(
                    'Intervalo de datas invalido. '
                    f'Intervalo maximo permitido: {utils.MAX_DATA_RANGE}.'
                )
            )

        if self.is_coin_invalid(coin):
            exceptions.append(ValidationError(f'Moeda invalida: "{coin}".'))

        if exceptions:
            raise ValidationError(exceptions)

        return cleaned_data
