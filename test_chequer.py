from chequer import (
    get_decimals,
    get_digits,
    )

import unittest


class GetDigitsGetDecimalsTest(unittest.TestCase):

    def test_get_digits_for_number_with_no_decimals(self):
        self.assertEqual(get_digits('123'), '123')

    def test_get_digits_for_number_with_decimals(self):
        self.assertEqual(get_digits('456.78'), '456')

    def test_get_decimals_for_number_with_decimals(self):
        self.assertEqual(get_decimals('321.45'), '45')

    def test_get_decimals_for_number_with_no_decimals(self):
        self.assertEqual(get_decimals('567'), None)
