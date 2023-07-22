from django import forms


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
