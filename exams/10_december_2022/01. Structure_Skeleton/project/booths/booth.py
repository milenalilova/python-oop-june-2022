from abc import ABC, abstractmethod

from project.core.validator import Validator


class Booth(ABC):
    PRICE_PER_PERSON = 0

    @abstractmethod
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.validate_value_not_negativ(value, 'Capacity cannot be a negative number!')
        self.__capacity = value

    @property
    @abstractmethod
    def type(self):
        return

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.PRICE_PER_PERSON * number_of_people
        self.is_reserved = True
