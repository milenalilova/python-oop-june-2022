from project.car.car import Car
from project.core.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_value_has_min_length(value.strip(), 1, 'Name should contain at least one character!')
        self.__name = value

    def change_car(self, new_car, old_car):
        old_car.is_taken = False
        self.car = new_car
        new_car.is_taken = True
        return f"Driver {self.name} changed his car from {old_car.model} to {new_car.model}."
