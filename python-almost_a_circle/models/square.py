#!/usr/bin/python3
"""
This module contains the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains instantiation of the class
    who inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function is the instantiation of the
        square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string representation of square
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        This function returns the width
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        This function sets the width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This function assigns values and attributes
        """
        if len(args):
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                if a == 1:
                    self.size = b
                if a == 2:
                    self.x = b
                if a == 3:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        This function contains the dictionary representation
        of the square
        """
        square = {}
        square["id"] = self.id
        square["size"] = self.size
        square["x"] = self.x
        square["y"] = self.y

        return (square)
