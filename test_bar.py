import unittest
from Bar import year_num_of_reg


class TestBar(unittest.TestCase):

    def test_year_compRegCount(self):
        result = {
            2001: 12,
            2002: 17,
            2013: 42,
            2019: 56,
            2020: 45,
            2021: 57
        }
        test_year = [2001, 2002, 2013, 2019, 2020, 2021]
        test_comp_reg_count = [12, 17, 42, 56, 45, 57]

        year = []
        comp_reg_count = []

        year_num_of_reg(result, year, comp_reg_count)
        self.assertEqual(year, test_year)
        self.assertEqual(comp_reg_count, test_comp_reg_count)


if __name__ == '__main__':
    unittest.main()
