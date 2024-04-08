from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        area = pi * (self.__radius ** 2)
        return area

    def calculate_perimeter(self):
        perimeter = 2 * pi * self.__radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        area = self.__height * self.__width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__height + self.__width)
        return perimeter


