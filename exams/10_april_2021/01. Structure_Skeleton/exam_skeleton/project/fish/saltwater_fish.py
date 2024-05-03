from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INITIAL_SIZE = 5
    EAT_INCREMENTAL = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, SaltwaterFish.INITIAL_SIZE, price)


