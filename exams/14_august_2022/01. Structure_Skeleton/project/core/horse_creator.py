from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseCreator:
    horse_types = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def create_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.horse_types:
            horse = self.horse_types[horse_type](horse_name, horse_speed)
            return horse
