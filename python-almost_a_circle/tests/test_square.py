#!/usr/bin/python3
"""
This module contain all the test for the 
square class
"""
import unittest
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    """
    The class who contain all of our tests
    """

    def test_size(self):
        """
        Test for functioning size
        """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        """
        Test for functionning width
        """
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        """
        Test for functioning height
        """
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """
        Test for functioning x
        """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """
        Test for functioning y
        """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 2)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_mandatory_size(self):
        """
        Test that width is a mandatory arg
        """
        with self.assertRaises(TypeError):
            s = Square()

