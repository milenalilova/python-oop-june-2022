from project.core.horse_creator import HorseCreator
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_creator = HorseCreator()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f'Horse {horse_name} has been already added!')

        horse = self.horse_creator.create_horse(horse_type, horse_name, horse_speed)
        if horse:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f'Jockey {jockey_name} has been already added!')

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(hr.race_type == race_type for hr in self.horse_races):
            raise Exception(f'Race {race_type} has been already created!')

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.__find_last_horse_by_type(horse_type)
        jockey = self.__find_jockey_by_name(jockey_name)

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__find_race_by_type(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in horse_race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        horse_race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):
        horse_race = self.__find_race_by_type(race_type)

        if len(horse_race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner = sorted(horse_race.jockeys, key=lambda j: j.horse.speed, reverse=True)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __find_last_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.type == horse_type and not horse.is_taken:
                return horse
        raise Exception(f'Horse breed {horse_type} could not be found!')

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(f'Jockey {jockey_name} could not be found!')

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f'Race {race_type} could not be found!')
