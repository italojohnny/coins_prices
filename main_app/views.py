from django.shortcuts import render
from main_app import utils


def index(request):
    coin_name = 'jpy'
    context = {
        'rates': utils.get_rates(coin_name),
        'coin': coin_name,
    }
    return render(request, 'index.html', context)
