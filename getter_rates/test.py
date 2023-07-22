from django.test import TestCase
from getter_rates import get_by_date
from requests.exceptions import HTTPError
from datetime import date, timedelta


class GetterRatesTestCase(TestCase):
    def test_return_type(self):
        result = get_by_date()
        return_type = isinstance(result, dict)

        self.assertTrue(return_type, 'Tipo do retorno invalido')

    def test_coins_names(self):
        result = get_by_date()
        coins_names = [i for i in result.keys() if i != 'date']
        self.assertIn('brl', coins_names, 'moeda brl nao encontrada')
        self.assertIn('eur', coins_names, 'modea eur nao encontrada')
        self.assertIn('jpy', coins_names, 'moeda jpy nao encontrada')

    def test_good_date(self):
        yesterday = date.today() - timedelta(days=1)
        result = get_by_date(yesterday)
        return_type = isinstance(result, dict)
        self.assertTrue(return_type, 'Tipo do retorno invalido')

    def test_future_date(self):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        result = get_by_date(tomorrow)
        self.assertEqual(
            today, result.get('date'), 'Data diferente do esperado'
        )

    def test_good_string_date(self):
        today = str(date.today())
        result = get_by_date(today)
        self.assertEqual(
            today, str(result.get('date')), 'Data diferente do esperado'
        )

    def test_very_old_date(self):
        very_old_date = date(1500, 4, 22)
        status_code = None
        try:
            result = get_by_date(very_old_date)
            status_code = result.status_code
        except HTTPError as err:
            status_code = err.response.status_code

        self.assertEqual(
            status_code, 500, 'codigo de retorno diferente do esperado'
        )

    def test_bad_string_date(self):
        string = 'abcdefgh'
        status_code = None
        try:
            result = get_by_date(string)
            status_code = result.status_code
        except HTTPError as err:
            status_code = err.response.status_code

        self.assertEqual(
            status_code, 400, 'codigo de retorno diferente do esperado'
        )
