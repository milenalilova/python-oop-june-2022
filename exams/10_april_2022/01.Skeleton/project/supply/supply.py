from abc import ABC, abstractmethod

from project.validators import validate_non_empty_string, validate_value_not_negative


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_non_empty_string(value, 'Name cannot be an empty string.')
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        validate_value_not_negative(value, 'Energy cannot be less than zero.')
        self.__energy = value

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"

    @property
    @abstractmethod
    def type(self):
        return
