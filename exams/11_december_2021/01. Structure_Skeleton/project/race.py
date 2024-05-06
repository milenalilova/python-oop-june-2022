from project.core.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_value_has_min_length(value.strip(), 1, 'Name cannot be an empty string!')
        self.__name = value
