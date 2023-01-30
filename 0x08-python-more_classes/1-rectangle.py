#!/usr/bin/python3
"""This module defines a rectangle class with private instance attribute"""


class Rectangle:

    """class Rectangle that defines a rectangle figure """

    def __init__(self, width=0, height=0):
        """Init method for Rectangle"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Property height to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Property width to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
