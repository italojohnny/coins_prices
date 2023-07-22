from django.test import TestCase
from .models import RateModel
from datetime import date


class RateModelTestCase(TestCase):
    def test_good_case(self):
        day = date(2023, 3, 23)
        inserted = RateModel(date=day, brl=1.0, eur=2.0, jpy=3.0)
        inserted.save()
        consulted = RateModel.objects.filter(date=day).first()
        self.assertEqual(inserted, consulted)

    def test_insert_date_already_saved(self):
        day = date(2023, 1, 1)
        rates1 = {'brl': 1.0, 'eur': 2.0, 'jpy': 3.0}
        rates2 = {'brl': 4.0, 'eur': 5.0, 'jpy': 6.0}

        first = RateModel(date=day, **rates1)
        first.save()

        latest, fail = RateModel.objects.update_or_create(
            date=day, defaults=rates2
        )

        recovered = RateModel.objects.filter(date=day).first()

        self.assertNotEqual(first.brl, recovered.brl)
        self.assertEqual(latest.brl, recovered.brl)
