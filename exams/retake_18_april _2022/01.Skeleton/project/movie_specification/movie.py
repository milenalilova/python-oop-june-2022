from abc import ABC, abstractmethod

from project.user import User
from project.validators import validate_non_empty_string, validate_value_above_num, validate_value_is_of_type


class Movie(ABC):
    MIN_AGE_RESTRICTION = None

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        validate_non_empty_string(value, 'The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        validate_value_above_num(value, 1888, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        validate_value_is_of_type(value, User, 'The owner must be an object of type User!')
        self.__owner = value

    # @property
    # @abstractmethod
    # def age_restriction(self):
    #     return
    #
    # @age_restriction.setter
    # def age_restriction(self, value):
    #     pass

    @abstractmethod
    def details(self):

        return
