from abc import ABC, abstractmethod


class Booth(ABC):
    PRICE_PER_PERSON = 0

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number: int = booth_number
        self.capacity: int = capacity
        self.delicacy_orders: list = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self):
        ...

    # helper funcs below
    def leave_booth(self):
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    def calculate_bill(self):
        return sum([d.price for d in self.delicacy_orders]) + self.price_for_reservation
