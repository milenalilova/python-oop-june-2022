from abc import ABC, abstractmethod

from project.validators import validate_non_empty_string, validate_value_not_negative_or_zero


class BaseFish(ABC):
    EAT_INCREMENTAL = 5

    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_non_empty_string(value, 'Fish name cannot be an empty string.')
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        validate_non_empty_string(value, 'Fish species cannot be an empty string.')
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        validate_value_not_negative_or_zero(value, 'Price cannot be equal to or below zero.')
        self.__price = value

    def eat(self):
        self.size += self.EAT_INCREMENTAL
