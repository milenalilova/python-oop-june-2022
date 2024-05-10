from project.core.validator import Validator


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_non_empty_string(value, 'Band name should contain at least one character!')
        self.__name = value

    def __str__(self):
        return f'{self.name} with {len(self.members)} members.'
