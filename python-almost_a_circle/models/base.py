#!/usr/bin/python3
"""
In this module, there is the base class
"""


class Base:
    """
    The class base, who gonna be our model for
    the whole project
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Our init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
