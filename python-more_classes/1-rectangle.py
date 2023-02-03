#!/usr/bin/python3
"""
This module defines a class - Rectangle
"""


class Rectangle:
    """
    This class has two attributes
    width
    height
    both will have property and setter function definition
    """

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function to return width if setter checks have passedr
        """
        return self.__width

    @property.setter
    def width(self, value):
        """
        setter validates if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if width is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        return self.__width = value

    @property
    def height(self):
        """
        function to return height if setter checks have passed
        """
        return self.__height

    @property.setter
    def height(self, value):
        """
        setter validates if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if height is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        return self.__height = value
