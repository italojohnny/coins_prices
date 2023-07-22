from django.shortcuts import render
from .forms import FormIndex
from main_app import utils


def index(request):
    coin_name = 'jpy'

    form = FormIndex(initial={'coin': coin_name})

    context = {
        'rates': utils.get_rates(coin_name),
        'coin': coin_name,
        'form': form,
    }
    return render(request, 'index.html', context)
