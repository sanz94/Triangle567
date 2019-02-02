# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #added test cases

    def testInput(self):
        self.assertNotEqual(classifyTriangle(300, 300, 300), 'InvalidInput')

    def testNegatives(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput')
        self.assertEqual(classifyTriangle(1, -1, 1), 'InvalidInput')

    def testFloat(self):
        self.assertNotEqual(classifyTriangle(1.5, 1.5, 1.5), 'InvalidInput')

    def testValidTriangle(self):
        self.assertNotEqual(classifyTriangle(2, 3, 4), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(3, 2, 4), 'NotATriangle')
        self.assertEqual(classifyTriangle(2, 3, 10), 'NotATriangle')

    def testTriangleType(self):
        self.assertNotEqual(classifyTriangle(2, 2, 4), 'Equilateral')
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')
        self.assertNotEqual(classifyTriangle(2, 2, 4), 'Right')
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertNotEqual(classifyTriangle(2, 4, 2), 'Scalene')
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene')
        self.assertNotEqual(classifyTriangle(2, 4, 3), 'Isoceles')
        self.assertEqual(classifyTriangle(2, 2, 4), 'Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

