#!/usr/bin/python3
"""
In this module, there is the base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This functions returns the json string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """
        This function writes the json
        string representation of list_objs
        to a file
        """
        jf = cls.__name__ + ".json"
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(cls.to_dictionary(i))
        with open(jf, mode="w") as myFile:
            myFile.write(cls.to_json_string(obj))
