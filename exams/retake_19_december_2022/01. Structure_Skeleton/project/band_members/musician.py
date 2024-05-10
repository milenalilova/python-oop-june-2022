from abc import ABC, abstractmethod

from project.core.validator import Validator


class Musician(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_non_empty_string_or_white_space(value, 'Musician name cannot be empty!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.validate_value_above_num(value, 16, 'Musicians should be at least 16 years old!')
        self.__age = value

    @property
    @abstractmethod
    def type(self):
        return

    @property
    @abstractmethod
    def skills_available(self):
        return

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.skills_available:
            raise ValueError(f'{new_skill} is not a needed skill!')
        if new_skill in self.skills:
            raise Exception(f'{new_skill} is already learned!')
        self.skills.append(new_skill)
        return f'{self.name} learned to {new_skill}.'
