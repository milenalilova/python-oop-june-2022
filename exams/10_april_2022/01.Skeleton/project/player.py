from project.validators import validate_non_empty_string, validate_value_above_num, validate_value_in_range, \
    validate_value_is_unique


class Player:
    DEFAULT_STAMINA = 100
    used_names = set()

    def __init__(self, name: str, age: int, stamina=DEFAULT_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_non_empty_string(value, 'Name not valid!')
        validate_value_is_unique(value, self.used_names, f'Name {value} is already used!')
        self.used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        validate_value_above_num(value, 12, 'The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        validate_value_in_range(value, 0, 100, 'Stamina not valid!')
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
