from django.shortcuts import render
from .forms import FormIndex
from main_app import utils
from datetime import date, timedelta


def index(request):
    coin_name = 'jpy'
    date2 = date.today()
    date1 = date2 - timedelta(days=4)
    rates = None

    form = FormIndex(initial={'coin': coin_name})

    rates = utils.get_rates(coin_name, date1, date2)

    context = {
        'rates': rates,
        'coin': coin_name,
        'form': form,
    }
    return render(request, 'index.html', context)
