from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    INITIAL_CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, SaltwaterAquarium.INITIAL_CAPACITY)

    @property
    def fish_type(self):
        return 'SaltwaterFish'
