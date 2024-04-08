from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_HORSE_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed < 120:
            self.speed = 120


horse1 = Appaloosa('Apala', 120)
print(horse1.name)
print(horse1.speed)
# print(horse1.max_speed_limit)
horse1.train()
print(horse1.speed)
horse1.train()
print(horse1.speed)


