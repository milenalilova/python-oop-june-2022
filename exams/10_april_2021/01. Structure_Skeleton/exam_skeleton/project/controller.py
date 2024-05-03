from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != 'FreshwaterAquarium' and aquarium_type != 'SaltwaterAquarium':
            return 'Invalid aquarium type.'

        aquarium = None
        if aquarium_type == 'FreshwaterAquarium':
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type != 'Ornament' and decoration_type != 'Plant':
            return 'Invalid decoration type.'

        decoration = None
        if decoration_type == 'Ornament':
            decoration = Ornament()
        elif decoration_type == 'Plant':
            decoration = Plant()

        self.decorations_repository.decorations.append(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_obj_by_name(aquarium_name, self.aquariums)
        decoration = self.__find_obj_by_type(decoration_type, self.decorations_repository.decorations)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium and decoration:
            aquarium.add_decoration(decoration)
            self.decorations_repository.decorations.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != 'FreshwaterFish' and fish_type != 'SaltwaterFish':
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_obj_by_name(aquarium_name, self.aquariums)
        fish = None

        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
            if aquarium is not None:
                return aquarium.add_fish(fish)
        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
            if aquarium is not None:
                return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_obj_by_name(aquarium_name, self.aquariums)
        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_obj_by_name(aquarium_name, self.aquariums)

        fish_value = sum([f.price for f in aquarium.fish])
        decorations_value = sum([d.price for d in aquarium.decorations])
        aquarium_value = fish_value + decorations_value

        return f"The value of Aquarium {aquarium_name} is {aquarium_value:.2f}."

    def report(self):
        output = ''
        for aq in self.aquariums:
            output += str(aq) + '\n'
        return output.strip()

    @staticmethod
    def __find_obj_by_name(obj_name, obj_list):
        for obj in obj_list:
            if obj.name == obj_name:
                return obj

    @staticmethod
    def __find_obj_by_type(obj_type, obj_list):
        for obj in obj_list:
            if obj.__class__.__name__ == obj_type:
                return obj
