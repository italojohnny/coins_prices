from django.test import TestCase
from getter_rates import get_by_date


class GetterRatesTestCase(TestCase):

    def test_return_type(self):
        result = get_by_date()
        return_type = isinstance(result, dict)
        self.assertTrue(return_type, 'Tipo do retorno invalido')
