import unittest

from parameterized import parameterized
from app.money_format import MoneyFormat

# Following the AAA test case format (Arrange, Act, Assert)
# and test case parameterisation


class TestMoneyFormat(unittest.TestCase):

    def setUp(self):
        local_format = 'de_DE'
        self.money_format_under_test = MoneyFormat(local_format)

    # Positive Test Cases

    def test_can_format_float_to_local(self):
        # Arrange
        given_value = 10.00
        expected_value = '10,00 EUR'

        # Act
        observed_value = self.money_format_under_test.format(given_value)

        # Assert
        self.assertIn(expected_value, observed_value)

    @parameterized.expand(
        [
            (
                "currency symbol", 10.00, 'EUR',
                "currency should contain the Eu symbol"
            ),
            (
                "separator", 10.00, ',',
                "currency should contain the , separator"
            ),
            (
                "two points of precision", 10.1234, '12',
                "currency should contain the two points of precision"
            ),
            (
                "no first value given", .1234, '0,12 EUR',
                "currency should contain a leading 0, even when none is given"
            ),
        ])
    def test_can_format_float_to_local_with(self, _, given_value,
                                            expected_value, message):
        # Act
        observed_value = self.money_format_under_test.format(given_value)

        # Assert
        self.assertIn(expected_value, observed_value)

    # Negative Test Cases

    @parameterized.expand(
        [
            (
                'empty string', ''
            ),
            (
                'string formatted number', '10.00'
            ),
            (
                'int number', 1
            ),
            (
                'None', None
            ),
        ])
    def test_error_is_thrown_when_given(self, _, given_value):

        with self.assertRaises(TypeError) as context:
            # Act
            self.money_format_under_test.format(given_value)

        # Assert
        self.assertTrue('argument: "amount" must be a float'
                        in str(context.exception))
