from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

ornament = Ornament()
plant = Plant()
decoration_repository = DecorationRepository()
controller = Controller()

# fresh_water_fish = FreshwaterFish('Pepo', 'carp', 5)
# salted_water_fish = SaltwaterFish('Fifa', 'salmon', 15)
freshwater_aquarium = FreshwaterAquarium('FrAqua')
# saltwater_aquarium = SaltwaterAquarium('SAqua')
print(controller.add_decoration('Ornament'))
print(controller.decorations_repository.decorations)
print(controller.add_aquarium('SaltwaterAquarium', 'SAqua'))
print(controller.insert_decoration('SAqua', 'Ornament'))
# print(controller.add_fish('SAqua', 'SaltwaterFish', 'Pipi', 'carp', 5))

# print(controller.feed_fish('SAqua'))
# print(controller.calculate_value('SAqua'))
print(controller.report())


