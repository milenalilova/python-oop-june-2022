class Robot:
    SENSORS = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return Robot.SENSORS


class MedicalRobot(Robot):
    SENSORS = 6

    def __init__(self, name):
        super().__init__(name)


class ChefRobot(Robot):
    SENSORS = 4

    def __init__(self, name):
        super().__init__(name)


class WarRobot(Robot):
    SENSORS = 12

    def __init__(self, name):
        super().__init__(name)


def number_of_robot_sensors(robot):
    return robot.SENSORS


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

print(basic_robot.SENSORS)
print(da_vinci.SENSORS)
print(moley.SENSORS)
print(griffin.SENSORS)

print(number_of_robot_sensors(basic_robot))
print(number_of_robot_sensors(da_vinci))
print(number_of_robot_sensors(moley))
print(number_of_robot_sensors(griffin))
