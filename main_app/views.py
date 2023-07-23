from django.shortcuts import render
from .forms import FormIndex
from main_app import utils
from datetime import date, timedelta


def index(request):
    coin_name = 'jpy'
    date2 = date.today()
    date1 = date2 - timedelta(days=4)
    rates = None
    error_flag = False

    if request.method == "POST":
        form = FormIndex(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['begin']
            date2 = form.cleaned_data['end']
            coin_name = form.cleaned_data['coin']
        else:
            error_flag = True
    else:
        form = FormIndex(
            initial={
                'begin': date1.strftime(utils.DATE_FORMAT),
                'end': date2.strftime(utils.DATE_FORMAT),
                'coin': coin_name,
            }
        )

    if not error_flag:
        rates = utils.get_rates(coin_name, date1, date2)

    context = {
        'rates': rates,
        'coin': coin_name,
        'form': form,
    }
    return render(request, 'index.html', context)
