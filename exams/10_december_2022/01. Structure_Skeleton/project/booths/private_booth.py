from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.5

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    @property
    def type(self):
        return 'PrivateBooth'
