from project.horse_race import HorseRace


class RaceFactory:
    race_types = [
        'Winter',
        'Spring',
        'Autumn',
        'Summer',
    ]

    def create_race(self, name):
        if name not in self.race_types:
            raise ValueError('Race type does not exist!')
        race = HorseRace(name)
        return race
