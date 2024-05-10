from project.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def skills_available(self):
        return ['sing high pitch notes', 'sing low pitch notes']

    @property
    def type(self):
        return 'Singer'
