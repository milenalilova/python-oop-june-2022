from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    SPEED_INCREMENTAL = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed_limit(self):
        return 140

    def train(self):
        if self.speed <= self.max_speed_limit - self.SPEED_INCREMENTAL:
            self.speed += self.SPEED_INCREMENTAL
        elif self.speed < self.max_speed_limit:
            self.speed = self.max_speed_limit
