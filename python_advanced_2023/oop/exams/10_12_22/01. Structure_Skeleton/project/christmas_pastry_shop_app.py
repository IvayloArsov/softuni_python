from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    deli_dict = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    booth_dict = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    # helper func - find obj by name in the given array of data
    @staticmethod
    def find_obj_by_name(obj_name, arr):
        obj = [obj for obj in arr if obj.name == obj_name]
        return obj[0] if obj else None

    @staticmethod
    def find_obj_by_number(obj_num, arr):
        obj = [obj for obj in arr if obj.booth_number == obj_num]
        return obj[0] if obj else None

    @staticmethod
    def find_suitable_booth(arr, capacity):
        obj = [obj for obj in arr if obj.is_reserved is False and obj.capacity >= capacity]
        return obj[0] if obj else None

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        new_deli = self.find_obj_by_name(name, self.delicacies)
        if new_deli:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.deli_dict:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        new_deli = self.deli_dict[type_delicacy](name, price)
        self.delicacies.append(new_deli)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        new_booth = self.find_obj_by_number(booth_number, self.booths)
        if new_booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.booth_dict:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth = self.booth_dict[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        booth = self.find_suitable_booth(self.booths, number_of_people)
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_obj_by_number(booth_number, self.booths)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = self.find_obj_by_name(delicacy_name, self.delicacies)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = self.find_obj_by_number(booth_number, self.booths)
        bill = booth.calculate_bill()
        self.income += bill
        booth.leave_booth()
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
