import unittest
from app import calculate_total


class TestPayment(unittest.TestCase):

    def test_calculate_total(self):
        result = calculate_total(1000, 50)
        self.assertEqual(result, 1050)


if __name__ == "__main__":
    unittest.main()