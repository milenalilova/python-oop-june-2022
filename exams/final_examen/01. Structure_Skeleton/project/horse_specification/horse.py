from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    SPEED_INCREMENTAL = 0

    # @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_less_than(value, 4, f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.raise_if_number_is_bigger_than_max_number(value, self.max_speed_limit, "Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_speed_limit(self):
        return

    @abstractmethod
    def train(self):
        pass
        # if self.speed <= self.max_speed_limit - self.SPEED_INCREMENTAL:
        #     self.speed += self.SPEED_INCREMENTAL
        # elif self.speed < self.max_speed_limit:
        #     self.speed = self.max_speed_limit

        # The method below raises Value Error(it shouldn't) because it runs the Validator.
        # Probably it runs the @setter

        # self.speed += self.SPEED_INCREMENTAL
        # if self.speed > self.max_speed_limit:
        #     self.speed = self.max_speed_limit
