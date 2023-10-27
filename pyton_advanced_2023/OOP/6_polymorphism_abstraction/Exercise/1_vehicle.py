from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity
        self.air_con_consumption = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.air_con_consumption)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity
        self.air_con_consumption = 1.6
        self.fuel_leak = 0.95

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.air_con_consumption)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.fuel_leak

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
