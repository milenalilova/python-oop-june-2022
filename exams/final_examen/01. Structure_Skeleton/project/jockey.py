from project.core.validator import Validator


class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.validate_if_number_less_then_eighteen(value, "Jockeys must be at least 18 to participate in the race!")
        self.__age = value






