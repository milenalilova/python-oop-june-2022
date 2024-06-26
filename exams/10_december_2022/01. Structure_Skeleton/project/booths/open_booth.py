from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.5

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    @property
    def type(self):
        return 'OpenBooth'
