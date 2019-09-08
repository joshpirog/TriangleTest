# -*- coding: utf-8 -*-
"""
@author: Joshua Pirog

"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    def testValidTriangle(self):
        self.assertEqual(classifyTriangle(4,2,10),'NotATriangle')
    
    def testValidInput(self):
        self.assertEqual(classifyTriangle(201, 500, -5), 'InvalidInput')
        
    def testIsIntegers(self):
        self.assertEqual(classifyTriangle("apple", "pear", "fig"), 'InvalidInput')
        
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(8, 7, 5), 'Scalene')
    
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(5, 7, 5), 'Isosceles')
        
    
        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)

