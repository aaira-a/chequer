from chequer import (
    get_decimals,
    get_digits,
    parse_single_digit,
    parse_two_digits,
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


class ParseSingleDigitTest(unittest.TestCase):

    def test_1_to_9(self):
        expected_results = {
            '1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat',
            '5': 'lima', '6': 'enam', '7': 'tujuh', '8': 'lapan',
            '9': 'sembilan'}

        for key in expected_results.keys():
            self.assertEqual(parse_single_digit(key), expected_results[key])


class ParseTwoDigitsTest(unittest.TestCase):

    def test_exact_multiple_of_10s(self):
        expected_results = {
            '10': 'sepuluh', '20': 'dua puluh', '30': 'tiga puluh',
            '40': 'empat puluh', '50': 'lima puluh', '60': 'enam puluh',
            '70': 'tujuh puluh', '80': 'lapan puluh', '90': 'sembilan puluh'}

        for key in expected_results.keys():
            self.assertEqual(parse_two_digits(key), expected_results[key])
