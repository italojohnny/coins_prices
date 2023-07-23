from django.test import TestCase, Client
from django.urls import reverse
from . import utils
from .models import RateModel
from .forms import FormIndex
from datetime import date, timedelta


GOOD_COIN = 'brl'
BAD_COIN = 'xxx'

MONDAY = date(2023, 7, 17)
FRIDAY = date(2023, 7, 21)
SUNDAY = date(2023, 7, 16)
GOOD_DATE = MONDAY
BAD_DATE = SUNDAY
GOOD_DATE_RANGE = (MONDAY, FRIDAY)
BAD_DATE_RANGE = (MONDAY, MONDAY + timedelta(days=30))
OLD_DATE_RANGE = (date(1500, 1, 1), date(1500, 1, 5))
GOOD_FORM = {
    'begin': GOOD_DATE_RANGE[0],
    'end': GOOD_DATE_RANGE[1],
    'coin': GOOD_COIN,
}
BAD_FORM = {
    'begin': BAD_DATE_RANGE[0],
    'end': BAD_DATE_RANGE[1],
    'coin': BAD_COIN,
}
OLD_FORM = {
    'begin': OLD_DATE_RANGE[0],
    'end': OLD_DATE_RANGE[1],
    'coin': GOOD_COIN,
}


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


class UtilsTestCase(TestCase):
    def test_get_rates_good_way(self):
        result = utils.get_rates(GOOD_COIN, GOOD_DATE)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 1)

        r = result[0]
        self.assertTrue(isinstance(r.get('date'), date))
        self.assertTrue(isinstance(r.get('value'), float))

    def test_get_rates_bad_coin(self):
        result = utils.get_rates(BAD_COIN)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 1)

        r = result[0]
        self.assertTrue(isinstance(r.get('date'), date))
        self.assertTrue(isinstance(r.get('value'), type(None)))

    def test_get_rates_bad_date(self):
        result = utils.get_rates(GOOD_COIN, BAD_DATE)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 1)

        r = result[0]
        self.assertTrue(isinstance(r.get('date'), date))
        self.assertTrue(isinstance(r.get('value'), float))
        self.assertNotEqual(r.get('date'), BAD_DATE)

    def test_get_rates_good_date_range(self):
        result = utils.get_rates(GOOD_COIN, *GOOD_DATE_RANGE)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(len(result), 5)

    def test_get_rates_bad_date_range(self):
        self.assertRaises(
            utils.InvalidDateRange,
            utils.get_rates,
            GOOD_DATE,
            *BAD_DATE_RANGE,
        )


class FormIndexTestCase(TestCase):
    def test_good_case(self):
        form = FormIndex(data=GOOD_FORM)
        self.assertTrue(form.is_valid())

    def test_bad_case(self):
        form = FormIndex(data=BAD_FORM)
        self.assertFalse(form.is_valid())


class ViewIndexTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_index_good_case(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_index_bad_case(self):
        response = self.client.post(self.url, BAD_FORM)
        self.assertRegex(response.content.decode(), r'inv.lid.')

    def test_index_old_bad_case(self):
        response = self.client.post(self.url, OLD_FORM)
        self.assertEqual(response.status_code, 200)
