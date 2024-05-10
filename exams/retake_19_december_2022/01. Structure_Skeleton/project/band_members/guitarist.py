from project.band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def skills_available(self):
        return ['play metal', 'play rock', 'play jazz']

    @property
    def type(self):
        return 'Guitarist'
