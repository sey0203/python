import unittest

def Calculator(a, b):
    return a + b

def Subtract(a, b):
    return a - b

class TestCalculaotr(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator
        self.subtract = Subtract

    def test_add(self):
        result = self.calculator(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.subtract(5, 1)
        self.assertNotEqual(result, 3)

    def tearDown(self):
        self.calculator = None
        self.subtract = None