import unittest
from companyReg2015 import dist_count_of_reg


class TestCompanyReg2015(unittest.TestCase):

    def test_dist_compReg2015(self):
        result = {
            'Aurangabad': 198,
            'Parbhani': 12,
            'Jalgaon': 52,
            'Akola': 22,
            'Latur': 68,
            'Ahmednagar': 50,
            'Kolhapur': 36,
            'Sangli': 44,
            'Thane': 459,
            }
        test_dist = ['Aurangabad', 'Parbhani', 'Jalgaon', 'Akola', 'Latur',
                     'Ahmednagar', 'Kolhapur', 'Sangli', 'Thane']
        test_compReg2015_count = [198, 12, 52, 22, 68, 50, 36, 44, 459]

        dist = []
        comReg2015_count = []

        dist_count_of_reg(result, dist, comReg2015_count)
        self.assertEqual(dist, test_dist)
        self.assertEqual(comReg2015_count, test_compReg2015_count)


if __name__ == '__main__':
    unittest.main()
