import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from math import inf
from src.Math import Math

class MathTest(unittest.TestCase):
    
    math = None

    @classmethod
    def setUpClass(self):
        self.math = Math()

    def test_sum(self): 
        self.assertEqual(self.math.sum(3, 2), 5)

    def test_sub(self): 
        self.assertEqual(self.math.sub(1, 1), 0)

    def test_mul(self): 
        self.assertEqual(self.math.mult(2, 3), 6)

    def test_div(self): 
        self.assertEqual(self.math.div(17, 2), 8.5)
    
    def test_divByZero(self): 
        self.assertEqual(self.math.div(2, 0), inf)

    def test_divFloor(self): 
        self.assertEqual(self.math.divFloor(17.5, 2), 8)
    
    def test_divFloorByZero(self): 
        self.assertEqual(self.math.divFloor(3.5, 0), inf)

    def test_mod(self): 
        self.assertEqual(self.math.mod(10, 2), 0)

    def test_modByZero(self): 
        self.assertIsNone(self.math.mod(2, 0))

if __name__ == '__main__':
    #https://pypi.org/project/MutPy/
    unittest.main()