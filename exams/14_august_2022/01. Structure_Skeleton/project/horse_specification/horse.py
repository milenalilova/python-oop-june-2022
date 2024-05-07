from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    MAXIMUM_SPEED = 0
    SPEED_INCREMENTAL = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_length_above_minimum(value, 4, f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.validate_value_does_not_exceed_limit(value, self.MAXIMUM_SPEED, 'Horse speed is too high!')
        self.__speed = value

    def train(self):
        self.speed = min(self.speed + self.SPEED_INCREMENTAL, self.MAXIMUM_SPEED)

    @property
    @abstractmethod
    def type(self):
        return
