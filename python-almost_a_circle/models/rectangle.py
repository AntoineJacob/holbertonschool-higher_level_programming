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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        returns the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        return the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        returns the x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        returns the y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        setter validates value is an integer > 0
        receives value as parameter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area value
        """
        return(self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle
        instance with the character # with x and y
        """
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                             ("#" * self.__width))
                                            for a in range(self.__height)))

    def __str__(self):
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """function to assign args to attribute
        """
        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.width = b
                if a == 2:
                    self.height = b
                if a == 3:
                    self.x = b
                if a == 4:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
