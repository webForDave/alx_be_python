import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(1, 3), 4)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(12, 6), 6)
        self.assertEqual(self.calc.subtract(6, 12), -6)
        self.assertEqual(self.calc.subtract(10, 3), 7)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(10, -2), -20)
        self.assertEqual(self.calc.multiply(-7, -5), 35)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(100, 2), 50)

    
    def test_divide_by_zero(self):
        return self.assertEqual(self.calc.divide(10, 0), None)