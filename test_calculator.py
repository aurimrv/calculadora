from unittest import TestCase
from calculator import mul

class CalculatorTest(TestCase):
    def test_mul(self):
        self.assertEqual(mul(2, 2), 4)

    def test_mul2(self):
        self.assertEqual(mul(3, 2), 6)        