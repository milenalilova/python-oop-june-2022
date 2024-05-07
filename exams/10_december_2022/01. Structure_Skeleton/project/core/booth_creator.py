from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class BoothCreator:
    booth_types = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def create_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.booth_types:
            raise Exception(f'{type_booth} is not a valid booth!')
        booth = self.booth_types[type_booth](booth_number, capacity)
        return booth
