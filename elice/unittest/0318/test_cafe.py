import unittest
from src.cafe import apply_coupon

class TestCafe(unittest.TestCase):
    def setUp(self):
        self.original_price = 10000

    def tearDown(self):
        self.original_price = None

    def test_apply_10_coupon(self):
        result = apply_coupon(self.original_price, 10)
        self.assertEqual(result, 9000)
    
    def test_apply_50_coupon(self):
        result = apply_coupon(self.original_price, 50)
        self.assertEqual(result, 5000)

    def test_invalid_coupon(self):
        with self.assertRaises(ValueError):
            apply_coupon(self.original_price, 150)