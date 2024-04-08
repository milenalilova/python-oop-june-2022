from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    DRIVE_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += Car.DRIVE_INCREASE
        distance_allowed = self.fuel_quantity / self.fuel_consumption
        if distance > distance_allowed:
            return
        self.fuel_quantity -= distance * self.fuel_consumption
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    DRIVE_INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += Truck.DRIVE_INCREASE
        distance_allowed = self.fuel_quantity / self.fuel_consumption
        if distance > distance_allowed:
            return
        self.fuel_quantity -= distance * self.fuel_consumption
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel
        return self.fuel_quantity
