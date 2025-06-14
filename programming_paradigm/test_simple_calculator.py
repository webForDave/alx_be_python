import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):

    def setUp(self):
        self.cal = SimpleCalculator()


    def test_add(self):
        self.assertEqual(self.cal.add(10, 5), 15)
        self.assertEqual(self.cal.add(2, 4), 6)
        self.assertEqual(self.cal.add(1, 3), 4)
    
    def test_subtract(self):
        self.assertEqual(self.cal.subtract(12, 6), 6)
        self.assertEqual(self.cal.subtract(6, 12), -6)
        self.assertEqual(self.cal.subtract(10, 3), 7)
    
    def test_multiply(self):
        self.assertEqual(self.cal.multiply(2, 4), 8)
        self.assertEqual(self.cal.multiply(10, -2), -20)
        self.assertEqual(self.cal.multiply(-7, -5), 35)
    
    def test_divide(self):
        self.assertEqual(self.cal.divide(100, 2), 50)

    
    def test_divide_by_zero(self):
        return self.assertEqual(self.cal.divide(10, 0), None)