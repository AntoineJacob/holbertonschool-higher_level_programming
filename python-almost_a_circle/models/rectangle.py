#!/usr/bin/python3
"""
This module contain our rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Our class Rectangle with differents args
    who inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Our constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    """
    return the width
    """
    return(self.__width)


@width.setter
def width(self, value):
    """width: width of the rectangle
    setter validating width is int and >= 0
    Raise:
        TypeError and ValueError
    """
    if type(value) is not int:
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = value


@property
def height(self):
    """
    return the height
    """
    return(self.__height)


@height.setter
def height(self, value):
    """height: height of the rectangle
    setter validating height is int and >= 0
    Raise:
        TypeError and ValueError
    """
    if type(value) is not int:
        raise TypeError("height must be an integer")
    elif value < 0:
            raise ValueError("heigh tmust be >= 0")
    else:
        self.__height = value


@property
def x(self):
    """
    return the x
    """
    return(self.__x)


@x.setter
def x(self, value):
    """x: x of the rectangle
    setter validating x is int and >= 0
    Raise:
         TypeError and ValueError
    """
    if type(value) is not int:
        raise TypeError("x must be an integer")
    elif value < 0:
        raise ValueError("x tmust be >= 0")
    else:
        self.__x = value


@property
def y(self):
    """
    return the y
    """
    return(self.__y)


@y.setter
def y(self, value):
    """y: y of the rectangle
    setter validating y is int and >= 0
    Raise:
         TypeError and ValueError
    """
    if type(value) is not int:
        raise TypeError("y must be an integer")
    elif value < 0:
                raise ValueError("y must be >= 0")
    else:
        self.__y = value
