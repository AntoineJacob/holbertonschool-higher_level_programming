#!/usr/bin/python3
""" module Rectangle """
from models.base import Base


class Rectangle(Base):
    """ define Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coorfinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        Raises:
            TypeError: if either of width, height, x or y is not an int
            ValueError: if either of width or height <= 0
            ValueError: if either of x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieve the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve the x coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve the y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the rectangle's area """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for i in range(self.__y):
                print()
        for j in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """ return [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ assign a key/value argument to attributes """
        if kwargs and kwargs != "":
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif args and args != "":
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """ return the dictionary representation of a Rectangle """
        a = ['id', 'width', 'height', 'x', 'y']
        b = [self.id, self.width, self.height, self.x, self.y]
        dict = {}
        for i in range(len(a)):
            dict[a[i]] = b[i]
        return dict
