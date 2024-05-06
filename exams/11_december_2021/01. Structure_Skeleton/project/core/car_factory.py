from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    car_types = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar
    }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.car_types:
            car = self.car_types[car_type](model, speed_limit)
            return car
