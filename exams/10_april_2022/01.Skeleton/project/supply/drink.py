from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_UNITS = 15

    def __init__(self, name):
        super().__init__(name, self.INITIAL_UNITS)

    @property
    def type(self):
        return 'Drink'
