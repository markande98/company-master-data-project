import unittest
from histogram import select_interval, set_intervals


class TestHistogram(unittest.TestCase):

    def test_choice(self):
        print("******Test for the user choice******")
        switcher = {
            1: "0 - 1L",
            2: "1L - 10L",
            3: "10L - 1Cr",
            4: "1Cr - 10Cr",
            5: ">10Cr"
        }
        result = select_interval()
        self.assertEqual(result[0], switcher.get(result[1]))

    def test_interval(self):
        print("******Test for the Interval******")
        interval1 = [0, 100000]
        interval2 = [100000, 1000000]
        interval3 = [1000000, 10000000]
        interval4 = [10000000, 100000000]
        interval5 = [100000000, 1000000000]

        result = select_interval()[0]
        test_interval = set_intervals(result)
        if result == "0 - 1L":
            self.assertEqual(interval1, test_interval)
        elif result == "1L - 10L":
            self.assertEqual(interval2, test_interval)
        elif result == "10L - 1Cr":
            self.assertEqual(interval3, test_interval)
        elif result == "1Cr - 10Cr":
            self.assertEqual(interval4, test_interval)
        else:
            self.assertEqual(interval5, test_interval)


if __name__ == '__main__':
    unittest.main()
