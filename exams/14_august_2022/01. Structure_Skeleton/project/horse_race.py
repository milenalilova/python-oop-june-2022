from project.core.validator import Validator


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        valid_types = ['Winter', 'Spring', 'Autumn', 'Summer']
        Validator.validate_type_is_valid(value, valid_types, 'Race type does not exist!')
        self.__race_type = value
