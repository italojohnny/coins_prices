from django.test import TestCase
from getter_rates import get_by_date


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
