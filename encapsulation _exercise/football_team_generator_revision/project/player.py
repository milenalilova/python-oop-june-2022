class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        output = f"Player: {self.__name}\n"
        output += f"Sprint: {self.__sprint}\n"
        output += f"Dribble: {self.__dribble}\n"
        output += f"Passing: {self.__passing}\n"
        output += f"Shooting: {self.__shooting}\n"
        return output.strip()
