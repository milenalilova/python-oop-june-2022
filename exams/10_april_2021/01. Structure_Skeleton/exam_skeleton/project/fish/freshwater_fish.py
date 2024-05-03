from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INITIAL_SIZE = 3
    EAT_INCREMENTAL = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, FreshwaterFish.INITIAL_SIZE, price)


