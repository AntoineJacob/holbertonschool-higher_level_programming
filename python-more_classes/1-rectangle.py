#!/usr/bin/python3
"""
This module defines a class - Rectangle
"""


class Rectangle:
    """
    This is a class who print a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property.setter
    def width(self, value):
        if width is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        return self.__width = value

    @property
    def height(self):
        return self.__height

    @property.setter
    def height(self, value):
        if height is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        return self.__height = value
