from django.shortcuts import render
from main_app import utils


def index(request):
    context = {
        'rates': utils.get_rates(),
    }
    return render(request, 'index.html', context)
