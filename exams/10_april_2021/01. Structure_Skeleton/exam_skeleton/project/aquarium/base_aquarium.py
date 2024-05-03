from abc import ABC, abstractmethod

from project.validators import validate_non_empty_string


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_non_empty_string(value, 'Aquarium name cannot be an empty string.')
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        total_comfort = sum([d.comfort for d in self.decorations])
        return total_comfort

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        if self.fish_type != fish.__class__.__name__:
            return 'Water not suitable.'
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = f'{self.name}:' + '\n'

        if not self.fish:
            output += f"Fish: none" + '\n'
        else:
            fish_names = [f.name for f in self.fish]
            output += f"Fish: {' '.join(fish_names)}" + '\n'

        output += f"Decorations: {len(self.decorations)}" + '\n'

        output += f"Comfort: {self.calculate_comfort()}"

        return output.strip()
        # fish_status = 'none' if len(self.fish) == 0 else ' '.join([f.name for f in self.fish])
        # return f'{self.name}:\n' + \
        #        f'Fish: {fish_status}\n' + \
        #        f'Decorations: {len(self.decorations)}\n' + \
        #        f'Comfort: {self.calculate_comfort()}'
