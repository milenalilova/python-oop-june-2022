from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class MusicianCreator:
    valid_types = {
        'Guitarist': Guitarist,
        'Drummer': Drummer,
        'Singer': Singer
    }

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_types:
            raise ValueError('Invalid musician type!')
        musician = self.valid_types[musician_type](name, age)
        return musician
