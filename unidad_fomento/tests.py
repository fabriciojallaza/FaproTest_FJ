import unittest
from datetime import date, datetime

from lib.uf_scrapper import UFScrapper


class TestUFScrapper(unittest.TestCase):
    def setUp(self):
        self.scrapper = UFScrapper()

    def test_get_uf_value_valid_date(self):
        # Test case for a valid date
        date_str = "2023-05-08"
        expected_value = 35943.26

        value = self.scrapper.get_uf_value(date_str)

        self.assertEqual(value, expected_value)

    def test_valid_date_first_day_of_month(self):
        # Test valid date (May 1, 2023)
        date_str = "2023-05-01"
        expected_value = 35851.62
        value = self.scrapper.get_uf_value(date_str)

        self.assertEqual(value, expected_value)

    def test_valid_date_last_day_of_month(self):
        # Test valid date (May 31, 2023)
        date_str = "2023-04-30"
        expected_value = 35838.55
        value = self.scrapper.get_uf_value(date_str)

        self.assertEqual(value, expected_value)

    def test_get_uf_value_invalid_date(self):
        # Test case for an invalid date
        date_str = "2023-02-30"

        with self.assertRaises(ValueError):
            self.scrapper.get_uf_value(date_str)

    def test_get_uf_value_future_date(self):
        # Test case for a future date
        date_str = str(date.today().year + 1) + "-01-01"

        with self.assertRaises(ValueError):
            self.scrapper.get_uf_value(date_str)

    def test_get_uf_value_no_value(self):
        # Test case for a date without a value
        date_str = "2025-05-10"

        with self.assertRaises(ValueError):
            self.scrapper.get_uf_value(date_str)

    def test_get_uf_value_month_not_loaded(self):
        # Test case for a date in a month that is not loaded yet
        date_str = "2023-06-01"

        with self.assertRaises(AttributeError):
            self.scrapper.get_uf_value(date_str)


if __name__ == "__main__":
    unittest.main()
