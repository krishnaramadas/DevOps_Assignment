#!/usr/bin/env python
# coding: utf-8

# In[1]:
#importing the defined calculator
import calculator as cal
#importing the unit test library
import unittest

#Test cases to test Calulator method
class test_Calculator(unittest.TestCase):   
    def test_add(self):
        self.assertEqual(cal.add(4,7), 11)
        self.assertEqual(cal.add(8,4), 12)
           
    def test_subtract(self):
        self.assertEqual(cal.subtract(4,7), -3)
        self.assertEqual(cal.subtract(8,4), 4)
        
    def test_multiply(self):
        self.assertEqual(cal.multiply(4,7),28)
        self.assertEqual(cal.multiply(8,4),32)
        
if __name__ == "__main__":
    unittest.main()






