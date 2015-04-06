from chequer import (
    get_decimals,
    get_digits,
    parse_single_digit,
    parse_three_digits,
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


class DictComparator(unittest.TestCase):

    def compare(self, function):

        for keys in self.expected_results.keys():
            self.assertEqual(function(keys), self.expected_results[keys])


class ParseSingleDigitTest(DictComparator):

    def test_1_to_9(self):
        self.expected_results = {
            '1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat',
            '5': 'lima', '6': 'enam', '7': 'tujuh', '8': 'lapan',
            '9': 'sembilan'}
        self.compare(parse_single_digit)


class ParseTwoDigitsTest(DictComparator):

    def test_exact_multiple_of_10s(self):
        self.expected_results = {
            '10': 'sepuluh', '20': 'dua puluh', '30': 'tiga puluh',
            '40': 'empat puluh', '50': 'lima puluh', '60': 'enam puluh',
            '70': 'tujuh puluh', '80': 'lapan puluh', '90': 'sembilan puluh'}
        self.compare(parse_two_digits)

    def test_teens(self):
        self.expected_results = {
            '11': 'sebelas', '12': 'dua belas', '13': 'tiga belas',
            '14': 'empat belas', '15': 'lima belas', '16': 'enam belas',
            '17': 'tujuh belas', '18': 'lapan belas', '19': 'sembilan belas'}
        self.compare(parse_two_digits)

    def test_non_10_multiples_non_teen(self):
        self.expected_results = {
            '53': 'lima puluh tiga', '99': 'sembilan puluh sembilan',
            '87': 'lapan puluh tujuh', '26': 'dua puluh enam'}
        self.compare(parse_two_digits)


class ParseThreeDigitsTest(DictComparator):

    def test_random_three_digits(self):
        self.expected_results = {
            '111': 'satu ratus sebelas',
            '153': 'satu ratus lima puluh tiga',
            '400': 'empat ratus',
            '530': 'lima ratus tiga puluh',
            '712': 'tujuh ratus dua belas'}
        self.compare(parse_three_digits)
