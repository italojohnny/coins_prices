from django.http import JsonResponse
from main_app.models import RateModel


def rates(request):
    data = [
        {'id': r.id, 'date': r.date, 'brl': r.brl, 'eur': r.eur, 'jpy': r.jpy}
        for r in RateModel.objects.all()
    ]
    return JsonResponse(data, safe=False)
