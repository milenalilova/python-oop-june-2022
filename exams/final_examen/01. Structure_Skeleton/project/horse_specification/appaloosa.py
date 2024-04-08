from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    SPEED_INCREMENTAL = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed_limit(self):
        return 120

    def train(self):
        if self.speed <= self.max_speed_limit - self.SPEED_INCREMENTAL:
            self.speed += self.SPEED_INCREMENTAL
        elif self.speed < self.max_speed_limit:
            self.speed = self.max_speed_limit

# horse1 = Appaloosa('Apala', 119)
# print(horse1.name)
# print(horse1.speed)
# print(horse1.max_speed_limit)
# horse1.train()
# print(horse1.speed)
