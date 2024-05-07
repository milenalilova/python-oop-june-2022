from abc import ABC, abstractmethod

from project.core.validator import Validator


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_non_empty_string_or_white_spaces(value, 'Name cannot be null or whitespace!')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.validate_value_not_negative_or_zero(value, 'Price cannot be less or equal to zero!')
        self.__price = value

    @property
    @abstractmethod
    def type(self):
        return

    def details(self):
        return f'{self.type} {self.name}: {self.portion}g - {self.price:.2f}lv.'
