import unittest
from groupBar import year_count, pba_count


class TestGroupBar(unittest.TestCase):

    def test_year(self):
        result = {
            2001: 12,
            2002: 17,
            2013: 42,
            2019: 56,
            2020: 45,
            2021: 57
        }
        test_year = [2001, 2002, 2013, 2019, 2020, 2021]
        test_year_reg_count = [12, 17, 42, 56, 45, 57]

        year = []
        year_reg_count = []

        year_count(result, year, year_reg_count)
        self.assertEqual(year, test_year)
        self.assertEqual(year_reg_count, test_year_reg_count)

    def test_pba(self):
        result = {
            'B1': 34,
            'B2': 67,
            'B3': 32,
            'B4': 56,
            'B5': 67,
            'B6': 78,
            'B7': 89
        }
        test_buisness = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
        test_buisness_count = [34, 67, 32, 56, 67, 78, 89]

        buisness = []
        buisness_count = []

        pba_count(result, buisness, buisness_count)
        self.assertEqual(buisness, test_buisness)
        self.assertEqual(buisness_count, test_buisness_count)


if __name__ == '__main__':
    unittest.main()
