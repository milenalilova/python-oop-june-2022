from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class DelicacyCreator:
    delicacy_types = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    def create_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.delicacy_types:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')
        delicacy = self.delicacy_types[type_delicacy](name, price)
        return delicacy
