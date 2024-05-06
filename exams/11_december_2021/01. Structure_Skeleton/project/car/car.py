from abc import ABC, abstractmethod

from project.core.validator import Validator


class Car(ABC):
    MIN_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.validate_value_has_min_length(value, 4, f'Model {value} is less than 4 symbols!')
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.validate_value_in_range(value, self.MIN_SPEED_LIMIT, self.MAX_SPEED_LIMIT, self.speed_limit_message)
        self.__speed_limit = value

    @property
    def speed_limit_message(self):
        return f"Invalid speed limit! Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!"

    @property
    @abstractmethod
    def type(self):
        return
