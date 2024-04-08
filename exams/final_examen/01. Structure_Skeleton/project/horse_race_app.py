from project.core.horse_factory import HorseFactory
from project.core.jockey_factory import JockeyFactory
from project.core.race_factory import RaceFactory
# from project.core.validator import Validator
# from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_factory = HorseFactory()
        self.jockey_factory = JockeyFactory()
        self.race_factory = RaceFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f'Horse {horse_name} has been already added!')
        try:
            horse = self.horse_factory.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse.__class__.__name__} horse {horse_name} is added."
        except RuntimeError:
            pass

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f'Jockey {jockey_name} has been already added!')
        # jockey = Jockey(jockey_name, age)
        # self.jockeys.append(jockey)
        # return f"Jockey {jockey_name} is added."
        try:
            jockey = self.jockey_factory.create_jockey(jockey_name, age)
            self.jockeys.append(jockey)
            return f"Jockey {jockey_name} is added."
        except RuntimeError:
            pass

    def create_horse_race(self, race_type: str):
        if race_type in [horse_race.race_type for horse_race in self.horse_races]:
            raise Exception(f'Race {race_type} has been already created!')
        try:
            horse_race = self.race_factory.create_race(race_type)
            self.horse_races.append(horse_race)
            return f"Race {race_type} is created."
        except RuntimeError:
            pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.__find_horse_by_type(horse_type)
        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'
        # self.horses.remove(horse)
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        race = self.__find_race_by_name(race_type)

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        # if not jockey.horse:
        #     raise Exception(f'Jockey {jockey_name} cannot race without a horse!')
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_name(race_type)

        if len(self.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        max_speed = 0
        winner = None
        horse_name = None
        for jockey in self.jockeys:
            # max_speed = 0
            # winner = None
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner = jockey
                horse_name = jockey.horse.name

        return f"The winner of the {race.race_type} race, " \
               f"with a speed of {max_speed}km/h is {winner.name}! Winner's horse: {horse_name}."

    def __find_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(f'Horse breed {horse_type} could not be found!')

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(f'Jockey {jockey_name} could not be found!')

    def __find_race_by_name(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f'Race {race_type} could not be found!')
