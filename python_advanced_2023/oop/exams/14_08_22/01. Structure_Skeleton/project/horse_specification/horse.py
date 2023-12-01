from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_HORSE_SPEED = None

    def __init__(self, horse_name: str, horse_speed: int):
        self.name = horse_name
        self.speed = horse_speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_HORSE_SPEED:
            raise ValueError(f"Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        ...