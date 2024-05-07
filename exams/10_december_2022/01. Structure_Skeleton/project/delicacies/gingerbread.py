from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)

    @property
    def type(self):
        return 'Gingerbread'
